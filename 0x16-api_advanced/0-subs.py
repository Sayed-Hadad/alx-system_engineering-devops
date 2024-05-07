#!/usr/bin/python3
import requests

"""
This module provides a function to fetch the number of subscribers from the Reddit API.
"""

def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit from the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers for the given subreddit. Returns 0 if the subreddit is invalid or if an error occurs.

    Raises:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/1.0.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
        
    except Exception as e:
        return 0
