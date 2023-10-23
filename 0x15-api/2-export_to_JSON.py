#!/usr/bin/python3
"""
create csv from api data of employee
"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    employee_id = sys.argv[1]

    # get employee name from api
    user_name = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_name = requests.get(user_name).json()
    user_name = user_name.get("username")

    # access all tasks
    todos = 'https://jsonplaceholder.typicode.com/todos/'
    todos_data = requests.get(todos).json()
    tasks_list = []
    for task in todos_data:
        if task.get('userId') == int(employee_id):
            to_add = {}
            completion = task.get('completed')
            title = task.get('title')
            to_add["task"] = title
            to_add["completed"] = completion
            to_add["username"] = user_name
            tasks_list.append(to_add)

    json_data = {}
    json_data[f'{employee_id}'] = tasks_list
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(json_data, f, indent=4)
