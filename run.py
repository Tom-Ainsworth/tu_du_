''' Run a to do list via a CLI '''

import json

with open('lists.json', 'r') as f:
    all_lists = json.load(f)


for task in all_lists['Lists'][0]['Example List']:
    print(task)
