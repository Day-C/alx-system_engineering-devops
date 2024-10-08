#!/usr/bin/python3
"""number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Query reddit api for subscribers of a subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 200:
        return 0
    return response.json().get("data").get("subscribers")
