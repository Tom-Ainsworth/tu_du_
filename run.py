'''Run a to do list via a CLI'''

from __future__ import print_function, unicode_literals
import json
import sys
from time import sleep

# from prompt_toolkit import prompt
from art import tprint
from PyInquirer import prompt

# Prompt list format
# questions = [
#         {
#             "type": "list",
#             "name": "question",
#             "message": "What would you like to do?"
#         }
#     ]


# def show_list_titles_as_list():
#     '''
#     Takes all keys from the ALL_LISTS constant and puts them into a list
#     '''

#     choices = [title for title in ALL_LISTS[0]]
#     questions[0].update({"choices": choices})


# def display_intro_text():
#     '''
#     Prints out introduction text to match the terminal rows/cols
#     '''

#     sleep(0.5)
#     print(f"{'=' * 80}")
#     tprint('               Welcome')
#     sleep(1)
#     tprint('                                    2')
#     sleep(1)
#     tprint('                      Tu_Du_')
#     print(f"{'=' * 80}")


# def delay_print(string):
#     '''
#     Prints out a string 1 character at a time to aid readability for users
#     '''

#     for character in string:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         sleep(0.05)
#     sleep(1)


# def show_main_menu():
#     '''
#     Displays the user options featured at the start of the app
#     '''

#     menu_choices = {"choices": [
#             "Create a New List", "Open Existing List", "Instructions Page"
#         ]
#     }
#     questions[0].update(menu_choices)

#     answer = prompt(questions).get("question")
#     if answer == "Create a New List":
#         list_name = input('Choose list name: ')
#         create_new_list(list_name)
#         delay_print(f'\nYour new list {list_name}has been created...')
#         delay_print(f'\nNow opening {list_name}...')
#     elif answer == "Open Existing List":
#         show_existing_lists()
#     else:
#         show_instructions_page()


# def main():
#     '''
#     Main function to run on app openings
#     '''

#     display_intro_text()
#     delay_print(
#         '\n          The productivity app that helps you manage your tasks\n'
#         )
#     show_main_menu()


# main()
new_data = {}
test_list = {"User List 2": ["a", "b", "c"]}
with open('lists.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    data["Lists"][-1].update(test_list)
    new_data.update(data)
print(new_data)
with open('lists.json', 'w', encoding="utf8") as f:
    json.dump(new_data, f, indent=4)
    print('data dumped')
