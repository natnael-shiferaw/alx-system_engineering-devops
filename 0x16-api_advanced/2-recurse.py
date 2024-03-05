#!/usr/bin/python3

"""
This module defines a recursive function to query the Reddit
API and return a list containing the titles of all hot articles
for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles
            (default empty).
        after (str): A token indicating the start of the next page
            (default None).
        count (int): The total count of articles fetched so far (default 0).

    Returns:
        list: A list containing the titles of all hot articles for
            the given subreddit, or None if the subreddit is invalid.
    """
    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set custom User-Agent header to avoid rate limiting
    headers = {"User-Agent": "Custom Reddit Recurse Function"}

    # Parameters for pagination and limiting the response
    params = {"after": after, "count": count, "limit": 100}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the subreddit is invalid
        if response.status_code == 404:
            return None

        # Extract data from the response
        data = response.json().get("data")

        # Get the token for the next page
        after = data.get("after")

        # Increment the total count of articles
        count += data.get("dist")

        # Extract titles of hot articles and append them to the list
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        # If there are more pages, recursively call the function
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        else:
            # If no more pages, return the list of hot article titles
            return hot_list
    except Exception as e:
        # If an exception occurs, return None
        return None
