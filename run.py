'''Run a to do list via a CLI'''

from __future__ import print_function, unicode_literals
import json
import sys
from time import sleep

# from prompt_toolkit import prompt
from art import tprint
from PyInquirer import prompt

with open('lists.json', 'r', encoding="utf-8") as f:
    lists_json_file = json.load(f)

# Constants
ALL_LISTS = lists_json_file['Lists']
LIST_TITLES = [title for title in ALL_LISTS[0]]
EXAMPLE_LIST_TITLE = LIST_TITLES[0]

# Prompt list format
main_menu = [
        {
            "type": "list",
            "name": "menu",
            "message": "What would you like to do?"
        }
    ]


def show_list_titles_as_list():
    '''
    Takes all keys from the ALL_LISTS constant and puts them into a list
    '''

    choices = [title for title in ALL_LISTS[0]]
    main_menu[0].update({"choices": choices})


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


def show_main_menu():
    '''
    Displays the user options featured at the start of the app
    '''

    menu_choices = {"choices": [
            "Create a New List", "Open Existing List", "Instructions Page"
        ]
    }
    main_menu[0].update(menu_choices)

    print(main_menu)

    answer = prompt(main_menu).get("menu")
    if answer == "Create a New List":
        list_name = input('Choose list name: ')
        create_new_list(list_name)
    elif answer == "Open Existing List":
        show_existing_lists()
    else:
        show_instructions_page()


def main():
    '''
    Main function to run on app openings
    '''

    display_intro_text()
    delay_print(
        '\n          The productivity app that helps you manage your tasks\n'
        )
    show_main_menu()


main()
