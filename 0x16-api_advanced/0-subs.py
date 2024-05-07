#!/usr/bin/python3
import requests

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

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.RequestException as e:
        return 0
    except KeyError as e:
        return 0
