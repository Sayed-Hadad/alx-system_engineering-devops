import requests


"""
Fetch number_of_subscribers From
Reddit Api
"""


def number_of_subscribers(subreddit):
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
