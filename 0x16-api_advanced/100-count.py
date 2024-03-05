#!/usr/bin/python3

"""
This module defines a recursive function to query the Reddit
API, parse the title of all hot articles, and print a sorted count
of given keywords.
"""

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    Recursively queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to search for in titles.
        found_list (list): A list to store the found keywords
            (default empty).
        after (str): A token indicating the start of the next page
            (default None).

    Returns:
        None
    """
    # Convert all keywords to lowercase
    word_list = [word.lower() for word in word_list]

    # Set custom User-Agent header to avoid rate limiting
    headers = {"User-Agent": "Custom Reddit Word Counter"}

    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Parameters for pagination
    params = {"after": after}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the subreddit is invalid
        if response.status_code == 404:
            print("Invalid subreddit or no posts found.")
            return

        # Extract data from the response
        data = response.json().get("data")

        # Get the token for the next page
        after = data.get("after")

        # Extract titles of hot articles
        for child in data.get("children"):
            title = child.get("data").get("title").lower()
            found_words = [word for word in word_list if word
                           in title.split()]
            found_list.extend(found_words)

        # If there are more pages, recursively call the function
        if after is not None:
            count_words(subreddit, word_list, found_list, after)
        else:
            # Count occurrences of each keyword
            keyword_count = {}
            for word in found_list:
                keyword_count[word] = keyword_count.get(word, 0) + 1

            # Print sorted count of keywords
            for keyword, count in sorted(keyword_count.items(),
                                         key=lambda x: (-x[1], x[0])):
                print(f"{keyword}: {count}")
    except Exception as e:
        print("An error occurred:", e)
