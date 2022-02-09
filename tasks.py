'''
Handle scenarios relating to viewing and editing lists & tasks
'''

import json

# Constants for reading lists.json file
file = open('lists.json', encoding="utf-8")
LISTS_CONTAINER = json.load(file)
ALL_LISTS = LISTS_CONTAINER["Lists"]


def create_new_list(list_name):
    '''
    Creates a list from a user input and dumps it into lists.json
    '''

    new_user_list = {list_name: []}
    ALL_LISTS[-1].update(new_user_list)
