#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests
import sys


def fetch_todo_list(employee_id):
    try:
        # Fetch user information
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        username = user_data['username']

        # Fetch TODO list for the employee
        todos_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        )
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare data for JSON export
        tasks = []
        for task in todos_data:
            task_info = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            tasks.append(task_info)

        data = {employee_id: tasks}

        # Write data to JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data exported to {json_filename} successfully.")

    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except KeyError:
        print("Error: Unexpected response structure")
    except ValueError:
        print("Error: Invalid JSON response")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
