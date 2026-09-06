import argparse
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'pending',
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully! (ID: {task['id']})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. You're all caught up!")
        return
    
    print(f"{'ID':<5} | {'Status':<10} | {'Description'}")
    print("-" * 50)
    for task in tasks:
        status_symbol = "[x]" if task['status'] == 'completed' else "[ ]"
        print(f"{task['id']:<5} | {status_symbol:<10} | {task['description']}")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completed'
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed!")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    initial_count = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    
    if len(tasks) < initial_count:
        # Reassign IDs to keep them sequential
        for index, task in enumerate(tasks):
            task['id'] = index + 1
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="A simple and efficient CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # List command
    parser_list = subparsers.add_parser("list", help="List all tasks")

    # Complete command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("id", type=int, help="ID of the task to complete")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
