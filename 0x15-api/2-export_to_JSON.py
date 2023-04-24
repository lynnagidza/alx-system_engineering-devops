#!/usr/bin/python3

"""
This module retrieves TODO list progress for a given employee ID from a REST API and
exports it in JSON format
"""

import json
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """
    Retrieve TODO list progress for a given employee ID from a REST API:
    param employee_id: integer representing the ID of the employee whose progress is to be retrieved
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)

        employee_name = todos[0]['username']
        print(
            f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

        tasks_data = []
        for task in todos:
            tasks_data.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            })

        with open(f"{employee_id}.json", mode='w') as json_file:
            json.dump({"USER_ID": tasks_data}, json_file)

        print(
            f"Exported TODO list progress for employee ID {employee_id} to {employee_id}.json")

    else:
        print(
            f"Error retrieving TODO list progress for employee ID {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)
    else:
        print(f"Usage: {sys.argv[0]} employee_id")
