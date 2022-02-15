'''Run a to do list via a CLI'''

import json
from time import sleep
from art import tprint
from PyInquirer import prompt

from instructions import show_instructions_page
from printing import delay_print, fast_delay_print

# Constants for reading lists.json file
file = open('lists.json', 'r', encoding="utf-8")
LISTS_CONTAINER = json.load(file)
ALL_LISTS = LISTS_CONTAINER["Lists"]
LIST_NAMES = ALL_LISTS[0].keys()

# Prompt list format
QUESTIONS = [
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


def show_existing_lists():
    '''
    Shows exisiting lists for users to open
    '''

    menu_choices = {
        "choices": LIST_NAMES
        }
    QUESTIONS[0].update(menu_choices)

    answer = prompt(QUESTIONS[0]).get("question")
    selected_list = ALL_LISTS[0][answer]
    # Stop Users from editing "Example List"
    if answer == "Example List":
        delay_print('Here are your Tu_Du_s:\n')
        for task in selected_list:
            fast_delay_print(f'{task}\n')
        menu_choices = {"choices": ["Return to Main Menu"]}
        QUESTIONS[0].update(menu_choices)
        answer = prompt(QUESTIONS[0]).get("question")
        if answer:
            show_main_menu()
    else:
        delay_print('Here are your Tu_Du_s:\n')
        for task in selected_list:
            fast_delay_print(f'{task}\n')
        task_options(selected_list)


def task_options(selected_list):
    '''
    Displays the options to add, or complete a task
    '''
    if not selected_list:
        delay_print('You have no Tu_Du_s...\n')
        menu_choices = {"choices": [
            "Add a Tu_Du_", "Return to Main Menu"
            ]
            }
        QUESTIONS[0].update(menu_choices)
        answer = prompt(QUESTIONS).get("question")
    else:
        menu_choices = {"choices": [
            "Add a Tu_Du_", "Complete a Tu_Du_", "Return to Main Menu"
            ]
            }
        QUESTIONS[0].update(menu_choices)
        answer = prompt(QUESTIONS).get("question")
    if answer == "Add a Tu_Du_":
        # Adds user inputted task, then shows the previous menu again
        while answer == "Add a Tu_Du_":
            task_name = input('Name your Tu_Du_ ')
            if not task_name.strip():
                delay_print("Error: Please choose a name for your Tu_Du_\n")
            else:
                delay_print(
                    f'\nYour new Tu_Du_: {task_name} is being added...'
                    )
                selected_list.append(task_name)
                delay_print(f'\n{task_name} has now been added\n')
                task_options(selected_list)
    elif answer == "Complete a Tu_Du_":
        menu_choices = {"choices": get_menu_options(selected_list)}
        QUESTIONS[0].update(menu_choices)
        answer = prompt(QUESTIONS).get("question")
        if answer == "Return to main menu":
            show_main_menu()
        else:
            delay_print(
                f"\nWell Done, You've completed your Tu_Du: {answer}!\n"
                )
            selected_list.remove(answer)
            delay_print(
                f'{answer} has been removed.\n'
                )
            task_options(selected_list)
    else:
        show_main_menu()


def get_menu_options(selected_list):
    '''
    Makes a copy of the tasks from selected_list, then appends
    the option "return to main menu" so users can leave the loop"
    '''

    menu_choices = selected_list.copy()
    menu_choices.append("Return to main menu")
    return menu_choices


def save_all_lists():
    '''
    Saves all current lists and tasks to lists.json
    for user to come back to later.
    '''
    new_list_data = {}
    new_list_data.update(LISTS_CONTAINER)

    with open('lists.json', 'w', encoding="utf-8") as updated_json:
        json.dump(new_list_data, updated_json, indent=4)
    LISTS_CONTAINER.update(new_list_data)


def reset_all_lists():
    '''
    Removes all user lists apart from example list
    '''

    starting_list_data = {
        "Lists": [
            {
                "Example List": [
                    "Brush my teeth",
                    "Go to the gym",
                    "Feed the cat",
                    "Book a haircut"
                ]
            }
        ]
    }
    with open('lists.json', 'w', encoding="utf-8") as updated_json:
        json.dump(starting_list_data, updated_json, indent=4)
    LISTS_CONTAINER.update(starting_list_data)
    global LIST_NAMES, ALL_LISTS
    ALL_LISTS = LISTS_CONTAINER["Lists"]
    LIST_NAMES = ALL_LISTS[0].keys()


def show_main_menu():
    '''
    Displays the user options featured at the start of the app
    '''

    menu_choices = {"choices": [
            "Instructions Page", "Create a New List", "Open Existing List",
            "Save All Lists", "Reset all Lists"
        ]
    }
    QUESTIONS[0].update(menu_choices)

    answer = prompt(QUESTIONS).get("question")
    if answer == "Instructions Page":
        show_instructions_page()
        menu_choices = {"choices": ["Return to main menu"]}
        QUESTIONS[0].update(menu_choices)
        answer = prompt(QUESTIONS).get("question")
        if answer == "Return to main menu":
            show_main_menu()
    while answer == "Create a New List":
        list_name = input('Choose list name: ')
        if not list_name.strip():
            delay_print("Error: Please choose a name for your list\n")
        else:
            delay_print(f'\nYour new list: {list_name} is being created...')
            new_user_list = {list_name: []}
            ALL_LISTS[-1].update(new_user_list)
            delay_print(f'\n{list_name} has now been created\n')
            show_main_menu()
    if answer == "Open Existing List":
        show_existing_lists()
    if answer == "Save All Lists":
        delay_print('Now saving all lists...\n')
        save_all_lists()
        delay_print('Your lists have been saved...\n')
        sleep(1)
        delay_print('Now returning to Main Menu...\n')
        sleep(1)
        show_main_menu()
    if answer == "Reset all Lists":
        delay_print("Resetting all User Lists...\n")
        reset_all_lists()
        delay_print(
            "All lists have been reset.\nNow returning to main menu\n"
            )
        show_main_menu()


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
