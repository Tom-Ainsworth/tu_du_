'''Run a to do list via a CLI'''

from __future__ import print_function, unicode_literals
import sys
import json
from time import sleep
from art import tprint
from PyInquirer import prompt

# Constants for reading lists.json file
file = open('lists.json', encoding="utf-8")
LISTS_CONTAINER = json.load(file)
ALL_LISTS = LISTS_CONTAINER["Lists"]

# Prompt list format
questions = [
        {
            "type": "list",
            "name": "question",
            "message": "What would you like to do?"
        }
    ]


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


def show_existing_lists():
    '''
    Shows exisiting lists for users to open
    '''

    list_titles = [title for title in ALL_LISTS[0]]
    menu_choices = {
        "choices": list_titles
        }
    questions[0].update(menu_choices)

    answer = prompt(questions[0]).get("question")
    selected_list = ALL_LISTS[0][answer]
    # Stop Users from editing "Example List"
    if answer == "Example List":
        delay_print('Here are your tasks:\n')
        tasks = [delay_print(f'{task}\n') for task in selected_list]
        menu_choices = {"choices": ["Return to Main Menu"]}
        questions[0].update(menu_choices)
        answer = prompt(questions[0]).get("question")
        if answer:
            show_main_menu()
    else:
        delay_print('Here are your tasks:\n')
        tasks = [delay_print(f'{task}\n') for task in selected_list]
        task_options(selected_list)


def task_options(selected_list):
    '''
    Displays the options to add, or complete a task
    '''

    menu_choices = {"choices": [
            "Add a Tu_Du_", "Complete a Tu_Du_", "Return to Main Menu"
        ]
    }
    questions[0].update(menu_choices)

    answer = prompt(questions).get("question")
    if answer == "Add a Tu_Du_":
        # Adds user inputted task and returns to main menu
        task_name = input('Name your Tu_Du_')
        delay_print(f'\nYour new Tu_Du_: {task_name} is being added...')
        selected_list.append(task_name)
        delay_print(f'\n{task_name} has now been added')
        show_main_menu()
    elif answer == "Complete a Tu_Du_":
        complete_task()
    else:
        show_main_menu()


def show_main_menu():
    '''
    Displays the user options featured at the start of the app
    '''

    menu_choices = {"choices": [
            "Create a New List", "Open Existing List", "Instructions Page"
        ]
    }
    questions[0].update(menu_choices)

    answer = prompt(questions).get("question")
    if answer == "Create a New List":
        list_name = input('Choose list name: ')
        delay_print(f'\nYour new list: {list_name} is being created...')
        new_user_list = {list_name: []}
        ALL_LISTS[-1].update(new_user_list)
        delay_print(f'\n{list_name} has now been created')
        show_main_menu()
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
        '\n          The productivity app that helps you manage your tasks\n\n'
        )
    show_main_menu()


main()
