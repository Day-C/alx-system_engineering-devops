#!usr/bin/python3
"""Query api and for info on a subject"""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API for number of subscribers of a 
    subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code > 300:
        return (0)
    else:
        response = response.json()
        data = response.data
        print(data.subscribers)
