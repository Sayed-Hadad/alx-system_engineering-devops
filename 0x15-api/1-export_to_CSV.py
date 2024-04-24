#!/usr/bin/python3

'''
Python script to export data in the CSV format.
'''
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users_url = url+f'users/{argv[1]}'
    todo_url = url+'todos'
    user = requests.get(users_url).json()
    todo_lis = requests.get(todo_url, params={'userId': argv[1]}).json()
    with open(f"{argv[1]}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for line in todo_lis:
            writer.writerow([argv[1], user.get('username'),
                            line.get('completed'), line.get('title')])
