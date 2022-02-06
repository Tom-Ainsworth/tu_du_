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

#     main_menu = [
#         {
#             "type": "list",
#             "name": "game",
#             "message": "What would you like to do?",
#             "choices": [
#                 "Create a New List",
#                 "See Instructions"
#             ]
#         }
#     ]

#     answer = prompt(main_menu).get("game")
#     if answer == "\n\nWhat would you like to do?":
#         create_new_list()
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
