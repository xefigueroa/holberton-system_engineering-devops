#!/usr/bin/python3
"""queries Reddit API, prints titles of 10 1st hot posts for subreddit."""

import requests


def top_ten(subreddit):
    """prints titles of 10 1st hot posts"""
    BASE_URL = 'http://www.reddit.com/r/{}/about.json'
    head = {'User-Agent': 'Mozilla/5.0'}
    par = {'limit': 10}

    r = requests.get(BASE_URL.format(subreddit), headers=head,
                     params=par, allow_redirect=False)

    data = r.json().get('data', {}).get('children', {})

    if data:
        for post in data:
            print(data.get('data').get('title'))
    else:
        print(None)
