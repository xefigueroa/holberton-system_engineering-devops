#!/usr/bin/python3
"""queries Reddit API, returns articles w/titles for subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """prints titles of 10 1st hot posts"""
    BASE_URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'Mozilla/5.0'}
    par = {'after': after}

    r = requests.get(BASE_URL, params=par, headers=head).json()

    res = r.get('data', {}).get('children', None)
    control = r.get('data', {}).get('after', None)

    if control is not None:
        if res:
            for hot in res:
                hot_list.append(hot.get('data').get('title'))
        if control is not None:
            recurse(subreddit, hot_list, control)
        return hot_list
    else:
        return None
