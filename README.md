# trello-activity-bot

Posts in a slack channel if Trello boards haven't been updated. This prevents
dead or abandoned boards from going unnoticed and ensures adherence to company
policy.

## Installation and Use
1. edit trellobot.config to contain your keys and preferences.  
2. Place trellobot.config in the directory ~/.trellobot/  
3. Run trellobot.py in a crontab  

crontab -e  
0 7 * * * /Users/eric/workspace/trello-activity-bot/trellobot.py   
