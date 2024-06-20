#!/usr/bin/python3
"""Module for task 1"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns thetitles of the first 10 hot posts listed for a given
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0
    else:
        sub_info = sub_info.json()
        for child in sub_info.data.children:
            print(child.get("data").get("title"))
