'''
Shows the instructions for Tu_Du
'''

from art import tprint
from printing import delay_print, fast_delay_print


def show_instructions_page():
    '''
    Displays the game instructions
    '''

    with open('instructions.txt', 'r', encoding="utf-8") as file:
        lines = file.read()
        delay_print(lines)

show_instructions_page()
