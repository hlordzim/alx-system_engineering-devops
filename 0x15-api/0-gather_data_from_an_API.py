#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""

import requests
import sys

def fetch_todo_list(employee_id):
    try:
        # Fetch user information
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        
        employee_name = user_data['name']
        
        # Fetch TODO list for the employee
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(done_tasks)
        
        # Display results
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    
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
