#!/usr/bin/python3
"""retive all hot post titles of a specific subreddit."""
import requests

def recurse(subreddit, host_list=[]):
    """recurcive function that queries api for all hot articles for
    specific sub reddit"

    
