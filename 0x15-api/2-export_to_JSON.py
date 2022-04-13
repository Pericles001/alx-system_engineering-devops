#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    todo_url = "https://jsonplaceholder.typicode.com/user/{}/todos".format(
        argv[1])
    name_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": name_result.get("username")})
        todo_list.append(todo_dict)

    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: todo_list}, f)
