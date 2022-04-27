#!/usr/bin/python3
"""

recursive function that queries the Reddit API, parses the title of all hot articles,
 and prints a sorted count of given keywords
"""

import requests

def count_words(subreddit, word_list):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print(0)
        return
    data = response.json()
    titles = []
    for post in data['data']['children']:
        titles.append(post['data']['title'])
    for word in word_list:
        count = titles.count(word)
        print('{}: {}'.format(word, count))
