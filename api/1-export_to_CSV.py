#!/usr/bin/python3
"""Python script that export data requested from an api to CSV file"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = eval(argv[1])
    filename = f'{user_id}.csv'
    count = 0
    tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    tasks_dict = tasks.json()
    users_dict = users.json()
    tasks_complete = []
    rows = []

    # Getting user name
    for user in users_dict:
        if user['id'] == user_id:
            user_name = str(user['username'])

    # Counting and adding task completed
    for task in tasks_dict:
        if task['userId'] == user_id:
            row = [user_id, user_name, task['completed'], task['title']]
            rows.append(row)

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # writing the data rows
        csvwriter.writerows(rows)
