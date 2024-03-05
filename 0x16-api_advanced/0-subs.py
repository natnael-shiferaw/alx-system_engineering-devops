#!/usr/bin/python3
"""
This module defines a function to retrieve the number
of subscribers for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    # Construct the URL for the subreddit's about page
    url = f'http://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent header to avoid rate limiting
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and return the number of subscribers
        return data.get('data').get('subscribers')
    else:
        # If the subreddit is invalid or the request fails, return 0
        return 0
