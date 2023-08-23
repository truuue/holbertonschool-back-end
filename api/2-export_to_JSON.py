#!/usr/bin/python3
"""Script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    employees_response = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    todos = todos_response.json()
    employees = employees_response.json()

    employee_name = None

    for employee in employees:
        if employee["id"] == employee_id:
            employee_name = employee["username"]
            break

    tasks_list = []

    for task in todos:
        if task.get("userId") == employee_id:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            }
            tasks_list.append(task_dict)

    json_object = {str(employee_id): tasks_list}
    filename = str(employee_id) + ".json"

    with open(filename, "w") as file:
        json.dump(json_object, file, indent=4)
