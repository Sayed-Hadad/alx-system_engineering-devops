#!/usr/bin/python3
"""
Count the number of subscribers to a subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for the given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The total number of subscribers for the given subreddit.
             Returns 0 if the subreddit is invalid or if an error occurs.
    """
    reddit_api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyAPI/1.0.0'}
    response = requests.get(reddit_api_url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    
    return 0

