#!/usr/bin/python3
"""retive data from api."""

def top_ten(subreddit):
    '''query reddit api for the titles fo the top ten hot posts
    listed for a given subreddit.'''

    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json/limit=10".format(subreddit),
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)

    if response.status_code >= 30:
        print("None")
    data = response.json()
    for key in data.keys():
        print(data[key].get('data').get('title'))
