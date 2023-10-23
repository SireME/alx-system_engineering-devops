#!/usr/bin/python3
"""
create json from api data of employee
"""

if __name__ == "__main__":
    import json
    import requests

    def name_from_id(employee_id):
        """get employee username from api"""
        user_name = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_name = requests.get(user_name).json()
        user_name = user_name.get("username")
        return user_name

    # access all tasks
    todos = 'https://jsonplaceholder.typicode.com/todos/'
    todos_data = requests.get(todos).json()

    tasks_list = []
    json_data = {}
    for i in range(len(todos_data)):
        current = todos_data[i].get('userId')
        previous = todos_data[i - 1].get('userId')
        if i != 0 and current != previous:
            json_data[f'{previous}'] = tasks_list
            tasks_list = []
        to_add = {}
        user_id = todos_data[i].get('userId')
        user_name = name_from_id(user_id)
        to_add["username"] = user_name
        completion = todos_data[i].get('completed')
        title = todos_data[i].get('title')
        to_add["task"] = title
        to_add["completed"] = completion
        tasks_list.append(to_add)
        if i == len(todos_data) - 1:
            json_data[f'{previous}'] = tasks_list

    with open(f'todo_all_employees.json', 'w') as f:
        json.dump(json_data, f, indent=4)
