#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
the data in CSV format"""

import csv
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

    for employee in employees:
        if employee["id"] == employee_id:
            employee_name = employee["name"]
            employee_username = employee["username"]
            break

    output_filename = f"{employee_id}.csv"
    with open(output_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get("userId") == employee_id:
                csv_writer.writerow(
                    [employee.get("id"), employee.get("username"),
                     task.get("completed"), task.get("title")])
