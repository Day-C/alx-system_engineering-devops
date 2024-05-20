#!/usr/bin/python3
'''Script sends a get request to a REST API.'''
import requests
import sys


def show_todo(id):
    '''Show_todo display the todo into about a user with id=id.'''

    url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'

    response = requests.get(url)
    data = response.json()
    tal= len(data)
    complt = 0

    for i in range(len(data)):
        if data[i].get('completed') == True:
            complt += 1

    print(f'Employee Ervin Howell is done with tasks({complt}/{tal}')
    for item in range(len(data)):
        if data[item].get('completed') == True:
            print('\t', data[item].get('title'))


if __name__ == "__main__":
    show_todo(sys.argv[1])
