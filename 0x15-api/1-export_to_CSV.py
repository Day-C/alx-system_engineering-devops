#!/usr/bin/python3
'''Script saves an api response into a file.'''
import requests
import sys


def save_as_csv(id):
    '''Saves api response.'''

    filename = f'{id}.csv'

    user_url = 'https://jsonplaceholder.typicode.com/users'
    list_url = f'https://jsonplaceholder.typicode.com/todos'

    # Get user info
    response1 = requests.get(f'{user_url}/{id}')
    user_info = dict(response1.json())
    name = user_info['username']

    # Get todo list info
    response2 = requests.get(f'{list_url}?userId={id}')
    data = response2.json()

    # organize and store in file
    for i in range(len(data)):
        completed = data[i].get('completed')
        title = data[i].get('title')
        csv = f'"{id}","{name}","{completed}","{title}"\n'

        with open(filename, 'a') as f:
            f.write(csv)


if __name__ == "__main__":
    save_as_csv(sys.argv[1])
