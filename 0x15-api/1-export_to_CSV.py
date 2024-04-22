#!/usr/bin/python3
""" Export to CSV """
import requests
from sys import argv


def export_to_csv(user_id):
    """ Export TODOS list progress for a given employee_id """
    api_url = 'https://jsonplaceholder.typicode.com/'
    todos_url = f'{api_url}/users/{user_id}/todos'
    users_url = f'{api_url}/users/{user_id}'

    todos_list = requests.get(todos_url).json()
    users_list = requests.get(users_url).json()

    username = users_list['username']

    with open(f'{user_id}.csv', mode='w', encoding='utf-8') as file:
        for task in todos_list:
            completed = task.get('completed')
            title = task.get('title')
            file.write(f'"{user_id}","{username}","{completed}","{title}"\n')


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_csv(int(argv[1]))
