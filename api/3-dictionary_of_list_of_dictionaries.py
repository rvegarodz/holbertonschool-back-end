#!/usr/bin/python3
"""Python script that export data requested from an api to JSON file"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    filename = 'todo_all_employees.json'
    tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    tasks_dict = tasks.json()
    users_dict = users.json()
    full_dict = {}

    # Getting user name
    for user in users_dict:
        dict_list = []
        user_id = user['id']
        username = user['username']
        # Counting and adding task completed
        for task in tasks_dict:
            if task['userId'] == user_id:
                task_dict = {'task': task['title'],
                             'completed': task['completed'],
                             'username': username}
                dict_list.append(task_dict)
        full_dict.update({user_id: dict_list})

    # writing to json file
    with open(filename, 'w') as jsonfile:
        # writing the data rows
        json.dump(full_dict, jsonfile)
