#!/usr/bin/python3

"""
This module retrieves TODO list progress for all employees from a REST API and
exports it in JSON format
"""

import json
import requests
import sys


def get_employee_todo_list_progress():
    """
    Retrieve TODO list progress for all employees from a REST API
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        todo_dict = {}
        for todo in todos:
            employee_id = todo['userId']
            employee_name = todo['username']
            task_title = todo['title']
            task_completed = todo['completed']

            if employee_id in todo_dict:
                todo_dict[employee_id].append(
                    {"username": employee_name, "task": task_title, "completed": task_completed})
            else:
                todo_dict[employee_id] = [
                    {"username": employee_name, "task": task_title, "completed": task_completed}]

        with open('todo_all_employees.json', mode='w') as json_file:
            json.dump(todo_dict, json_file)

        print("Exported TODO list progress for all employees to todo_all_employees.json")

    else:
        print("Error retrieving TODO list progress for all employees")


if __name__ == "__main__":
    get_employee_todo_list_progress()
