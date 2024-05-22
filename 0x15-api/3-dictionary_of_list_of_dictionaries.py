#!/usr/bin/python3
'''Script exoprts api response into json file.'''
import json
import requests


def save_all_to_json():
    '''Export data in json format.'''

    filename = 'todo_all_employees.json'
    user_url = 'https://jsonplaceholder.typicode.com/users'
    list_url = 'https://jsonplaceholder.typicode.com/todos'
    i = 1
    data = {}

    while i > 0:
        # Get user contents
        user_response = requests.get(f'{user_url}/{i}')
        user_info = user_response.json()
        if len(user_info) == 0:
            break
        name = user_info["username"]

        # Get list content
        list_response = requests.get(f'{list_url}?userId={i}')
        list_cont = list_response.json()

        tasks = []
        task = {}
        for item in range(len(list_cont)):
            task["username"] = name
            task["task"] = list_cont[item].get("title")
            task["completed"] = list_cont[item].get("completed")
            tasks.append(task)

        id = f"{i}"
        data[id] = tasks
        i += 1
    # Export to file
    with open(filename, 'w') as f:
        f.write(json.dumps(data))


if __name__ == "__main__":
    save_all_to_json()
