#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
