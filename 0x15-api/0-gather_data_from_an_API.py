#!/usr/bin/python3
"""
This module is a script that, uses a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys
    employee_id = sys.argv[1]

    # get employee name from api
    employee_name = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_name = requests.get(employee_name).json()
    employee_name = employee_name.get("name")

    # access all tasks
    todos = 'https://jsonplaceholder.typicode.com/todos/'
    todos_data = requests.get(todos).json()
    task_done = 0
    total_tasks = 0
    completed = []
    for task in todos_data:
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                task_done += 1
                completed.append("\t " + task.get('title'))

    status = f'Employee {employee_name} is done wi'
    status += f'th tasks({task_done}/{total_tasks}):'
    print(status)
    print("\n".join(completed))
