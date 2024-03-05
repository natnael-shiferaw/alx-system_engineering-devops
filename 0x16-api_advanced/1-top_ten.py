#!/usr/bin/python3

"""
This module defines a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent header to avoid rate limiting
    headers = {'User-Agent': 'Custom Reddit Top Ten Posts'}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the data from the response
            data = response.json().get('data', {}).get('children', [])

            # Print the titles of the first 10 hot posts
            for post in data[:10]:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid or the request fails, print None
            print("None")
    except Exception as e:
        # Print None if an exception occurs
        print("None")
