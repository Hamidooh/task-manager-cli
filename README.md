# CLI Task Manager

A simple, lightweight Command Line Interface (CLI) Task Manager built in Python. This project allows you to manage your daily tasks directly from your terminal.

## Features

- **Add Tasks**: Quickly add tasks to your to-do list.
- **List Tasks**: View all your tasks, including their current status (pending/completed).
- **Complete Tasks**: Mark tasks as done once you finish them.
- **Delete Tasks**: Remove tasks you no longer need.
- **Persistent Storage**: Saves your tasks locally in a `tasks.json` file.

## Prerequisites

- Python 3.x

## Usage

Navigate to the project directory in your terminal and run the script using Python.

### Add a Task
```bash
python tasker.py add "Buy groceries"
```

### List all Tasks
```bash
python tasker.py list
```

### Complete a Task
*(Use the ID shown when listing tasks)*
```bash
python tasker.py complete 1
```

### Delete a Task
```bash
python tasker.py delete 1
```

### Run Tests
```bash
python -m unittest discover -s tests
```

## Technologies Used

- Python (Built-in libraries: `argparse`, `json`, `os`, `datetime`, `unittest`)
