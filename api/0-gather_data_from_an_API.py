import requests
from sys import argv
"""Python script that, returns information for a given employee ID
about his/her TODO list progress"""

if __name__ == "__main__":
    user_id = eval(argv[1])
    count = 0
    tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    tasks_dict = tasks.json()
    users_dict = users.json()
    tasks_complete = []

    # Counting and adding task completed
    for task in tasks_dict:
        if task['userId'] == user_id:
            if task['completed']:
                count += 1
                tasks_complete.append(task['title'])

    # Getting user name
    for user in users_dict:
        if user['id'] == user_id:
            user_name = user['name']

    # Returns information about their progress
    print(f'Employee {user_name} is done with tasks({count}/20):')
    for i in tasks_complete:
        print(f'\t {i}')
