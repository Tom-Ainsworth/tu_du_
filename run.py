''' Run a to do list via a CLI '''

import json
import sys
from time import sleep
from art import tprint

with open('lists.json', 'r') as f:
    lists_json_file = json.load(f)

# Constants
ALL_LISTS = lists_json_file['Lists']
LIST_TITLES = list(ALL_LISTS[0].keys())
EXAMPLE_LIST_TITLE = ALL_LISTS[0].keys()


def display_intro_text():
    '''
    Prints out introduction text to match the terminal rows/cols
    '''

    sleep(0.5)
    print(f"{'=' * 80}")
    tprint('               Welcome')
    sleep(1)
    tprint('                                    2')
    sleep(1)
    tprint('                      Tu_Du_')
    print(f"{'=' * 80}")


def delay_print(string):
    '''
    Prints out a string 1 character at a time to aid readability for users
    '''

    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)
    sleep(1)


def main():
    '''
    Main function to run on app openings
    '''

    display_intro_text()
    delay_print('\n          The Productivity App that helps you manage your tasks')


main()
