#!/usr/bin/python3
"""
Print titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def print_list(items):
    for item in items:
        print(item)


def top_ten(subreddit):
    titles = []
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'ApiTraining'}
    response = requests.get(endpoint, headers=headers , allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data.get('data', {}).get('children', []):
            titles.append(post.get('data', {}).get('title', ''))
            if len(titles) == 10:
                break
        print_list(titles)
    else:
        print("None")
