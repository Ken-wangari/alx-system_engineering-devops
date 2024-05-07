#!/usr/bin/python3
"""
Recursively fetch hot article titles from Reddit for a subreddit; return None if no results.
"""

import requests

def get_hot_titles(subreddit, after=None):
    """
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    If no results are found for the given subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}

    params = {}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for bad status codes

        data = response.json()
        children = data.get("data", {}).get("children", [])

        if not children:
            return None  # No hot articles found

        titles = [child["data"]["title"] for child in children]

        # Recursive call to fetch more articles if available
        next_after = data.get("data", {}).get("after")
        if next_after:
            next_titles = get_hot_titles(subreddit, next_after)
            if next_titles is not None:
                titles.extend(next_titles)

        return titles

    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None
