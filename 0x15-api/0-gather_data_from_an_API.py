#!/usr/bin/python3
'''Script sends a get request to a REST API.'''
import requests
import sys


def show_todo(id):
    '''Show_todo display the todo into about a user with id=id.'''

    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    # Get user info
    user_response = requests.get(f'{user_url}/{id}')
    user_info = dict(user_response.json())
    name = user_info.get('name')

    # get todo list info
    list_response = requests.get(f'{todo_url}?userId={id}')
    tasks = list_response.json()

    # count completed tasks
    complete = 0
    total = len(tasks)
    for i in range(len(tasks)):
        if tasks[i].get('completed') is True:
            complete += 1

    # Display info about users todo list
    print(f'Employee {name} is done with tasks({complete}/{total}):')
    for item in range(len(tasks)):
        if tasks[item].get('completed') is True:
            print('\t', tasks[item].get('title'))


if __name__ == "__main__":
    show_todo(sys.argv[1])
