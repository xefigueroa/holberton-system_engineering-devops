#!/usr/bin/python3
"""queries Reddit API and returns number of subscribers for given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    BASE_URL = 'http://www.reddit.com/r/{}/about.json'
    head = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(BASE_URL.format(subreddit), headers=head)
    return r.json().get('data',{}).get('subscribers', 0)
