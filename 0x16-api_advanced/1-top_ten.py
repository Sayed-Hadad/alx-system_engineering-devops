#!/usr/bin/python3
"""
print the top ten posts titles
"""
import requests


def top_ten(subreddit):
    """
    print the top ten posts titles of a subreddit
    """
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9'
    headers = {'User-Agent': 'ApiTraining'}
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for title in data['data']['children']:
            print(title['data']['title'])
    else:
        print("None")
