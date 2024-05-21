#!/usr/bin/python3
'''Script saves an api response into a file.'''
import requests
import sys



def save_as_csv(id):
    '''Saves api response.'''

    filename = f'{id}.csv'

    #get todo info
    url = f'https://jsonplaceholder.typicode.com/users/{id}'

    response1 = requests.get(url)
    user_info = dict(response1.json())
    name = user_info['name']

    #get user info
    url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    
    response2 = requests.get(url)
    data = response2.json()

    for i in range(len(data)):
        completed = data[i].get('completed')
        title = data[i].get('title') 
        csv = f'"{id}", "{name}", "{completed}", "{title}"\n'

        with open(filename, 'a') as f:
            f.write(csv)


if __name__ == "__main__":
    save_as_csv(sys.argv[1])
