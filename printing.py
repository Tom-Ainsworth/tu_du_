'''
Gives different options for the delay print function
'''

import sys
from time import sleep


def delay_print(string):
    '''
    Prints out a string 1 character at a time to aid readability for users
    '''

    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)
    sleep(1)


def fast_delay_print(string):
    '''
    Prints out a string 1 character at a time to aid readability
    with a shorter gap between characters and items.
    '''

    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.03)
    sleep(0.5)
