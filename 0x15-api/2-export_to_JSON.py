#!/usr/bin/python3
""" EXport to JSON """
import json
import requests
from sys import argv


def export_to_json(user_id):
    """ Export JSON TODOS list progress for a given employee_id """
    api_url = 'https://jsonplaceholder.typicode.com/'
    todos_url = f'{api_url}/users/{user_id}/todos'
    users_url = f'{api_url}/users/{user_id}'

    todos_list = requests.get(todos_url).json()
    users_list = requests.get(users_url).json()

    username = users_list['username']

    with open(f'{user_id}.json', mode='w', encoding='utf-8') as file:
        json.dump({user_id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        } for task in todos_list]}, file)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_json(int(argv[1]))
