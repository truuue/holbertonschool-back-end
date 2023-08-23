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
    employee_username = None
    employee_completed_tasks = []
    json_object = {}
    tasks_list = []

    for employee in employees:
        if employee["id"] == employee_id:
            employee_name = employee["name"]
            employee_username = employee["username"]
            break

    for task in todos:
        if task.get("userId") == employee_id:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = employee.get("username")
            tasks_list.append(task_dict)

    json_object[str(employee.get("id"))] = tasks_list
    filename = str(employee.get("id")) + ".json"

    with open(filename, "w") as file:
        json.dump(json_object, file)
