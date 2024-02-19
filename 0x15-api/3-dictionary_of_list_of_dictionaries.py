#!/usr/bin/python3
"""
Exports to-do list information of all employees
to JSON format.
Requirements:
- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME",
                   "task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS},
                   {"username": "USERNAME", "task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS}, ... ],
                   "USER_ID": [ {"username": "USERNAME",
                   "task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS},
                   {"username": "USERNAME",
                   "task": "TASK_TITLE",
                   "completed": TASK_COMPLETED_STATUS}, ... ]
                   }
- File name must be: todo_all_employees.json
"""

import json
import requests


def fetch_employee_data():
    """Fetches employee information and their to-do lists."""
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch the list of all users (employees)
        users_response = requests.get(base_url + "users")
        users = users_response.json()

        # Create a dictionary containing to-do list info of all employees
        employee_data = {}
        for user in users:
            user_id = user["id"]
            user_url = base_url + f"todos?userId={user_id}"
            todo_response = requests.get(user_url)
            todo_list = todo_response.json()

            employee_data[str(user_id)] = [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username"),
                }
                for todo in todo_list
            ]

        return employee_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def export_to_json(data, filename="todo_all_employees.json"):
    """Exports data to a JSON file."""
    if data is None:
        print("No data to export.")
        return

    try:
        with open(filename, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)

    except IOError as e:
        print(f"Error exporting data: {e}")


if __name__ == "__main__":
    employee_data = fetch_employee_data()
    export_to_json(employee_data)
