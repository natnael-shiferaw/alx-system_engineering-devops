#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID
to JSON format.
Requirements:
- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS,
                   "username": "USERNAME"},
                   {"task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS,
                   "username": "USERNAME"}, ... ]
                   }
- File name must be: USER_ID.json
"""

import json
import requests
import sys


def export_to_json(user_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user_info.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    data_to_export = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_json(user_id)
