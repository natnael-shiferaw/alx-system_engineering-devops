#!/usr/bin/python3
"""Python script that returns about his/her TODO list progress
for a given employee ID.
- uses requests module
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = list()
    for t in todos:
        if t.get("completed") is True:
            completed.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print(f"\t {c}")
