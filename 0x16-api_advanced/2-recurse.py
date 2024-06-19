#!/usr/bin/python3
"""
return the list of all titles of hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """
    return the list of all titles of hot posts of a subreddit
    """
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'ApiTraining'}
    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for title in data['data']['children']:
            hot_list.append(title['data']['title'])
        if data['data']['after'] is not None:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
