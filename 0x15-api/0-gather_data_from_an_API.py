#!/usr/bin/python3

'''
 a Python script that, using this REST API,
 for a given employee ID, returns information
 about his/her TODO list progress.
'''
import requests
import sys



def fetch_todo_list_progress(employee_id):
    main_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{main_url}/users/{employee_id}'
    todo_url = f'{main_url}/todos?userId={employee_id}'

    # Fetch User Data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch User Data
    todos_response = requests.get(todo_url)
    todo_data = todos_response.json()

    # Count the completed tasks
    total_task = len(todo_data)
    completed_task = []
    for i in todo_data:
        if i['completed']:
            completed_task.append(1)

    # Print progress
    print(f'Employee {employee_name} is done with tasks({len(completed_task)}/{total_task}):')
    for task in todo_data:
        if task['completed']:
            print(f'\t{task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)
