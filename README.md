# Slack - Bot

This project was created out of a need to organize pinned items in our Slack channel by title. Note that our pinned items' titles are entered, precisely, with a prefixed date. This has enabled sorting for these pinned items, as Slack currently doesn't support sorted pinned items by date, as native channel functionality.

### Goal
1. Have the bot respond to the command 'shows' by returning all pinned items as:
	* PINNED_ITEM_TITLE - PINNED_ITEM_PERMALINK

### Technologies Used
* Python 3.6.2
* Django
* Django REST Framework
* Slack Client

### Slight Deviations from the below tutorials
* One thing I did was swap out the SLACK_BOT_USER_TOKEN for the SLACK_OAUTH_TOKEN. This token can be found in the OAuth & Permissions page for your app. It will be called OAuth Access Token. I needed this token because the Bot User OAuth Access Token, doesn't have access to the pins.read scope at this time. This scope is required for this Slack Bot.
* In Slack/settings.py, I made all the Slack tokens retrieved from environment variables. 
	* To configure these variables locally on UNIX, run:
		* export SLACK_BLAH_BLAH_BLAH_TOKEN='some_value_here'
	* To configure these variables on Heroku
		1. Go to Settings
		2. Config Variables, and press Reveal Config Vars
		3. Add the key name for your token, and the corresponding value

#### Heroku Specific Files
* Procfile
	* This tells Heroku what type of process it needs to run, and the command to run on the commandline
* runtime.txt
	* This tells Heroku what version of Python your Heroku app needs to run

#### Super-Helpful Tutorials
* Making a simple Django Slack App with a Bot
	* https://medium.com/freehunch/how-to-build-a-slack-bot-with-python-using-slack-events-api-django-under-20-minute-code-included-269c3a9bf64e
* Deploying a Django App to Heroku
	* https://devcenter.heroku.com/articles/deploying-python

Please feel free to fork this project and make pull requests!