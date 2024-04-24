#!/usr/bin/python3

'''
Python script to export data in the CSV format.
'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users_url = url+f'users/{argv[1]}'
    todo_url = url+'todos'
    user = requests.get(users_url).json()
    todo_lis = requests.get(todo_url, params={'userId': argv[1]}).json()
    data = {argv[1]: []}
    for task in todo_lis:
        task_dic = {'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': user.get('username')
                    }
        data[argv[1]].append(task_dic)
    with open(f"{argv[1]}.json", "w") as jsonfile:
        json.dump(data, jsonfile)
