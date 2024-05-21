#!/usr/bin/python3
'''Script exports user info into file.'''
import requests
import sys
import json


def save_to_json(id):
    '''export api response in json format.'''

    filename = f'{id}.json'
    user_url = 'https://jsonplaceholder.typicode.com/users'
    list_url = 'https://jsonplaceholder.typicode.com/todos'

    # get user info
    user_response = requests.get(f'{user_url}/{id}')
    info = dict(user_response.json())
    name = info['username']

    # get list info
    list_response = requests.get(f'{list_url}?userId={id}')
    data = list_response.json()

    # organize the data
    tasks = []
    tsk = {}
    for item in range(len(data)):
        tsk['task'] = data[item].get('title')
        tsk['completed'] = data[item].get('completed')
        tsk['username'] = name
        tasks.append(tsk)

    display = {}
    display[id] = tasks
    # export to file
    with open(filename, 'w') as f:
        f.write(json.dumps(display))


if __name__ == "__main__":
    save_to_json(sys.argv[1])
