#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for non-200 status codes
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return 0
        else:
            print(f"HTTP error occurred: {err}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

