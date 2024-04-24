#!/usr/bin/python3

'''
 a Python script that, using this REST API,
 for a given employee ID, returns information
 about his/her TODO list progress.
'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users_url = url+f'users/{argv[1]}'
    todo_url = url+'todos'
    user = requests.get(users_url).json()
    todo_lis = requests.get(todo_url, params={'userId': argv[1]}).json()
    todo_completed = []
    for task in todo_lis:
        if task.get('completed') is True:
            todo_completed.append(task.get('title'))
    print(
        f"Employee {user.get('name')}\
 is done with tasks({len(todo_completed)}/{len(todo_lis)}):")
    [print(f"\t {task}") for task in todo_completed]