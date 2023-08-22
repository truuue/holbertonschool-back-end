#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

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
    employee_completed_tasks = []

    for employee in employees:
        if employee["id"] == employee_id:
            employee_name = employee["name"]
            break

    for task in todos:
        if task["userId"] == employee_id and task["completed"]:
            employee_completed_tasks.append(task["title"])

    total_tasks = len(
        [task for task in todos if task["userId"] == employee_id])
    num_completed_tasks = len(employee_completed_tasks)

    print(f"Employee {employee_name} is done with tasks({
        len(num_completed_tasks)}/{len(total_tasks)}):")
    for completed_task in employee_completed_tasks:
        print("\t ", completed_task)
