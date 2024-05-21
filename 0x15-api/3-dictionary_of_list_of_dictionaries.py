#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests


def fetch_all_todos():
    try:
        # Fetch all users information
        users_url = "https://jsonplaceholder.typicode.com/users"
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()

        all_todos = {}

        for user in users_data:
            employee_id = user['id']
            username = user['username']

            # Fetch TODO list for the current employee
            todos_url = (
                f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )
            todos_response = requests.get(todos_url)
            todos_response.raise_for_status()
            todos_data = todos_response.json()

            # Prepare data for current employee
            tasks = []
            for task in todos_data:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                tasks.append(task_info)

            all_todos[employee_id] = tasks

        # Write data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_todos, json_file, indent=4)

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
    fetch_all_todos()
