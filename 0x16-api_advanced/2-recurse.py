#!/usr/bin/python3
"""
Task 2
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of titles of all hot articles."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        for post in posts:
            hot_list.append(post['data']['title'])

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
