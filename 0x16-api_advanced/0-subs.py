#!/usr/bin/python3
"""
count the number of subscribers to a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the nubmer of subscribers
    """
    endpoint = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'ApiTraining'}
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    return 0
