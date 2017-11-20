#!/usr/bin/python
import requests
from os.path import expanduser
import yaml
from trello import TrelloApi
import json
from datetime import datetime, timedelta

inactivityThreshold = 3 # in number of days

config_file = expanduser("~") + '/.trellobot/trellobot.config'
config = yaml.safe_load(open(config_file))

runDate = datetime.now().strftime("%Y-%m-%d")
runDateObj = datetime.now()

trello = TrelloApi(config['api-key'])
trello.set_token(config['api-token'])

boards = trello.organizations.get_board(config['org_name'])
message = []
for board in boards:
    bName = board['name']
    lastAct = board['dateLastActivity']
    if lastAct is not None and board['closed'] is not True:
        lastActObj = datetime.strptime(lastAct, "%Y-%m-%dT%H:%M:%S.%fZ")
        test = lastActObj.strftime("%Y-%m-%d")
        if runDateObj - timedelta(days = inactivityThreshold) > lastActObj:
            line = "Trello board " + bName + " hasn't had activity in " + \
                str(inactivityThreshold) + " days. :slightly_frowning_face:"
            message.append(line)
text = "\n".join(message)
print text
slack_payload = {
    "text": text,
    "channel": config['channel'],
    "icon_emoji": config['emoji'],
    "username": config['username']
}
# TODO: add error handling here
dow = datetime.today().weekday() # Monday is zero
if dow < 5: # weekday
    r = requests.post(config['slack_webhook_url'], data = json.dumps(slack_payload))
    print json.dumps(slack_payload, indent=2)
else:
    print "Not sending to slack because it's the weekend."
