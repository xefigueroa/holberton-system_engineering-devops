#!/usr/bin/python3
"""queries Reddit API, prints titles of 10 1st hot posts for subreddit."""

import requests


def top_ten(subreddit):
    """prints titles of 10 1st hot posts"""
    BASE_URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'Mozilla/5.0'}
    par = {'limit': 10}

    r = requests.get(BASE_URL, params=par, headers=head).json()

    res = r.get('data', {}).get('children', None)

    if res:
        for post in res:
            print(post.get('data').get('title'))
    else:
        print(None)
