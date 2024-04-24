#!/usr/bin/python3

'''
Python script to export data in the json format.
'''
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    all_data = {}
    for id in range(1, 11):
        users_url = url+f'users/{id}'
        todo_url = url+'todos'
        user = requests.get(users_url).json()
        todo_lis = requests.get(todo_url, params={'userId': id}).json()
        data = {id: []}
        for task in todo_lis:
            task_dic = {'task': task.get('title'),
                        'completed': task.get('completed'),
                        'username': user.get('username')
                        }
            data[id].append(task_dic)
        all_data.update(data)
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
