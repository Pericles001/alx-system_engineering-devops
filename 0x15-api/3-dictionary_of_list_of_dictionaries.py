#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_result = get(users_url).json()

    big_dict = {}
    for user in users_result:
        todo_list = []

        pep_fix = "https://jsonplaceholder.typicode.com"
        todos_url = pep_fix + "/user/{}/todos".format(user.get("id"))
        name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user.get("id"))

        todo_result = get(todos_url).json()
        name_result = get(name_url).json()
        for todo in todo_result:
            todo_dict = {}
            todo_dict.update({"username": name_result.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            todo_list.append(todo_dict)

        big_dict.update({user.get("id"): todo_list})

    with open("todo_all_employees.json", 'w') as f:
        dump(big_dict, f)
