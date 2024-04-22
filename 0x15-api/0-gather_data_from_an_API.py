#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


def get_todos_by_employee(employee_id):
    """ Return TODOS list progress for a given employee_id """
    api_url = 'https://jsonplaceholder.typicode.com/'
    todos_url = f'{api_url}/users/{employee_id}/todos'
    users_url = f'{api_url}/users/{employee_id}'

    todos_list = requests.get(todos_url).json()
    users_list = requests.get(users_url).json()

    user_name = users_list['name']

    completed = [task.get('title')
                 for task in todos_list if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(completed), len(todos_list)))

    for task in completed:
        print(f'\t {task}')


if __name__ == "__main__":
    if len(argv) == 2:
        get_todos_by_employee(int(argv[1]))
