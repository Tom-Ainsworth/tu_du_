'''
Shows the instructions for Tu_Du
'''

from time import sleep
from art import tprint
from printing import fast_delay_print


def show_instructions_page():
    '''
    Displays the game instructions
    '''

    fast_delay_print(f"{'=' * 80}\n\n")
    tprint('     Instructions\n                         Page\n\n')
    sleep(1)
    fast_delay_print(f"{'=' * 80}\n\n")
    sleep(0.5)
    with open('instructions.txt', 'r', encoding="utf-8") as file:
        lines = file.read()
        fast_delay_print(lines)
