#!/usr/bin/python3
"""
create csv from api data of employee
"""

if __name__ == "__main__":
    import requests
    import sys
    employee_id = sys.argv[1]

    # get employee name from api
    employee_name = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_name = requests.get(employee_name).json()
    employee_name = employee_name.get("username")

    # access all tasks
    todos = 'https://jsonplaceholder.typicode.com/todos/'
    todos_data = requests.get(todos).json()
    for task in todos_data:
        if task.get('userId') == int(employee_id):
            with open(f'{employee_id}.csv', "a") as file:
                completion = task.get('completed')
                f = f'\"{employee_id}\",\"{employee_name}\",\"{completion}\"'
                title = task.get('title')
                f += f',\"{title}\"'
                f += '\n'
                file.write(f)
