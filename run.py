''' Run a to do list via a CLI '''

import json
from art import *


tprint('TU DU')

with open('lists.json', 'r') as f:
    lists_json_file = json.load(f)

ALL_LISTS = lists_json_file['Lists']
LIST_TITLES = list(ALL_LISTS[0].keys())
EXAMPLE_LIST_TITLE = ALL_LISTS[0].keys()

