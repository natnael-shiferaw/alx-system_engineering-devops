#!/usr/bin/python3
"""Exports TODO list info for a given employee ID
in a CSV format.
Requirements:
- Records all tasks that are owned by the employee
- File name must be: USER_ID.csv
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS"
                 ,"TASK_TITLE"
"""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
