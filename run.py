''' Run a to do list via a CLI '''

import json
from art import *

def display_intro_text():
    '''
    Prints out introduction text to match the terminal rows/cols
    '''

    print(f"{'=' * 80}")
    tprint('               Welcome')
    tprint('                                    2')
    tprint('                      Tu_Du_')
    print(f"{'=' * 80}")

with open('lists.json', 'r') as f:
    lists_json_file = json.load(f)

ALL_LISTS = lists_json_file['Lists']
LIST_TITLES = list(ALL_LISTS[0].keys())
EXAMPLE_LIST_TITLE = ALL_LISTS[0].keys()

display_intro_text()