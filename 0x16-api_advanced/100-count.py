#!/usr/bin/python3
"""
Task 3 (advanced)
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively queries the Reddit API, parses titles, and prints a sorted count of keywords."""
    if after is None:
        counts = {word.lower(): 0 for word in word_list}

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
            title = post['data']['title'].lower().split()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    counts[word.lower()] += count

        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                if count > 0:
                    print(f"{keyword}: {count}")
    else:
        return None
