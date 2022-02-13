'''Handles all tasks relating to Creating, Updating and Deleting tasks'''

from __future__ import print_function, unicode_literals
from printing import delay_print


def add_new_task(selected_list):
    '''
    Adds a new task to the selected list
    '''

    task_name = input('Name your Tu_Du_ ')
    delay_print(f'\nYour new Tu_Du_: {task_name} is being added...')
    selected_list.append(task_name)
    delay_print(f'\n{task_name} has now been added')
