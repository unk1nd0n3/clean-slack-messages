#!/usr/bin/env python3
import os
import configparser

from slack_cleaner2 import *
from datetime import datetime

# Define global variables
COUNT = 0
DELETE_MESSAGES_OLDER_DAYS = 10
CURRENT_TIME = datetime.now()


def delta_days(message_time, current_time):
    """
    Calculate delta time between msg time and current time
    :param message_time: string
    :param current_time: datetime obj
    :return: int, str
    """
    message_datetime = datetime.fromtimestamp(int(float(message_time)))
    delta_date = current_time - message_datetime
    return delta_date.days, message_datetime.strftime("%m/%d/%Y, %H:%M:%S")


def delete_msgs_from_slack_objects(slack_conn, slack_object, delete_files):
    """
    Func to delete msg from particular Slack communication channel
    :param slack_conn: slack connection obj
    :param slack_object: slack communication object
    :param delete_files: bollean
    :return: boolean
    """
    global COUNT

    for msg in slack_conn.msgs(filter(match(str(slack_object)), slack_conn.conversations)):
        # delete messages, its files, and all its replies (thread)
        days, msg_time = delta_days(msg.json['ts'], CURRENT_TIME)
        # Delete messages older than DO_NOT_DELETE_MESSAGE_NEWER_DAYS
        if DELETE_MESSAGES_OLDER_DAYS <= days and msg.user_id == slack_conn.myself.id:
            print(f'Deleted MSG #{COUNT}. Time: {msg_time}. User: {str(slack_object)}. Text: {msg.text}.')
            msg.delete(replies=True, files=True)
            COUNT += 1
    return True


def main():
    """
    Main function
    :return:
    """
    # Set configuration file location
    main_script_abs = os.path.dirname(os.path.abspath(__file__))
    settings = configparser.ConfigParser()
    settings.read(main_script_abs + '/conf/settings.cfg')

    # Get Bamboo host and details
    slack_token = settings['SLACK']['token']

    # Authenticate to Slack
    slack_conn = SlackCleaner(slack_token)
    # # list of users
    # slack_conn.users
    # # list of all kind of channels
    # slack_conn.conversations

    # Delete all own messages in 1:1 with all users f
    for ims in slack_conn.ims:
        delete_msgs_from_slack_objects(slack_conn=slack_conn, slack_object=ims, delete_files=True)

    # Delete all own messages in multi-users-channels
    for mpim in slack_conn.mpim:
        delete_msgs_from_slack_objects(slack_conn=slack_conn, slack_object=mpim, delete_files=True)

    # Delete all own messages in groups
    for group in slack_conn.groups:
        delete_msgs_from_slack_objects(slack_conn=slack_conn, slack_object=group, delete_files=False)

    # Some examples
    # Delete all messages in -bots channels
    # for msg in slack_conn.msgs(filter(match('.*-bots'), slack_conn.conversations)):
    #     # delete messages, its files, and all its replies (thread)
    #     msg.delete(replies=True, files=True)
    #
    # # delete all general messages and also iterate over all replies
    # for msg in slack_conn.c.general.msgs(with_replies=True):
    #     msg.delete()


if __name__ == '__main__':
    main()
