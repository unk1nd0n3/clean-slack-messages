### What is this repository for? ###

This repo helps you to cleanup all own messages from Slack direct channels, multichannels and groups.

### Prerequisites ###

* Create virtual env
* Rename configuration template 
    ```bash
    cd clean-slack-messages
    cp conf/settings.cfg.template conf/settings.cfg
    ```
* Create an app in Slack [How to create Slack app]([This is an image](https://myoctocat.com/assets/images/base-octocat.svg))
* Get a token and save in configuration file
  ```bash
  clean-slack-messages/conf/settings.cfg
  ```
* Set variable DELETE_MESSAGES_OLDER_DAYS  


### How do I get set up a script? ###

* Clone repository
* Cd clean-slack-messages
* Install virtual env:
    ```bash
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements
    ```
* Run script (see section: Usage)


### Usage ###
* Use script with below arguments:
    ```bash
    Usage:
      main.py
    ```

### Reference ###
https://github.com/sgratzl/slack_cleaner2
