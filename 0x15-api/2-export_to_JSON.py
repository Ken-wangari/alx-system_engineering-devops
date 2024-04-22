#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_user_info(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    return response.json()

def get_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    try:
        user_info = get_user_info(user_id)
        todos = get_todos(user_id)
    except requests.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    
    print("Employee {} has completed {}/{} tasks:".format(user_info['name'], len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t", task)

