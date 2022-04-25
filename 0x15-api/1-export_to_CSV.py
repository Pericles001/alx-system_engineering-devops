#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": name_result.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
