#!/usr/bin/python3

'''
A Python script that, using this REST API,
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
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        e_n = user_data['name']
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)

    # Fetch Todo Data
    try:
        todos_response = requests.get(todo_url)
        todos_response.raise_for_status()
        t_data = todos_response.json()

        # Count the completed tasks
        cTasks = sum(1 for i in t_data if i['completed'])

        # Print progress
        print(f'Employee {e_n} is done with tasks({cTasks}/{len(t_data)}):')

        for task in t_data:
            if task['completed']:
                print(f'\t{task["title"]}')
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching todo data: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_list_progress(employee_id)
