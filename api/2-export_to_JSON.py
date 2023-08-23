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

    employee_id = int(sys.argv[1])
    json_object = {}
    tasks_list = []

    for employee in employees:
        if employee.get("id") == employee_id:
            our_employee = employee

    for task in todos:
        if task.get("userId") == employee_id:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = our_employee.get("username")
            tasks_list.append(task_dict)

    json_object[str(our_employee.get("id"))] = tasks_list
    filename = str(our_employee.get("id")) + ".json"

    with open(filename, "w") as file:
        json.dump(json_object, file)
