# Task-Tracker

Task Tracker CLI project from https://roadmap.sh/projects/task-tracker

## Features

- Create, read, update, and delete tasks
- Filter tasks by status (New, In Progress, Done)
- Save/load tasks to/from JSON files
- Command-line interface

## Technologies Used

- Python 3.13
- Standard libraries:
  - `datetime` - For task timestamps
  - `tkinter` - For file dialogs
  - `json` - For storing data

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TETROGAME/Task-Tracker.git
```

2. You are all set. No additional dependencies other than standard Python libraries required.

## Usage

Run the application using Python:

```bash
python main.py
```

### Main Menu Options

- `1` - Print tasks (with filtering options)
- `2` - Add a new task
- `3` - Edit an existing task
- `4` - Delete an existing task
- `s` - Save tasks to a JSON file
- `l` - Load tasks from a JSON file
- `sq` - Save and quit
- `q` - Quit without saving

### Task Statuses

Tasks can have one of the following statuses:
- `New`
- `In progress`
- `Done`

## Project Structure

- `TaskTracker.py` - Contains the core classes and functionality
  - `Task` class - Represents individual tasks
  - `TaskException` class - custom exception for errors with Task objects
  - `TaskTracker` class - Manages collections of tasks
  - `as_task` function - Helper for JSON deserialization
- `main.py` - Application entry point and CLI interface

## Example

```
Welcome to Task Tracker, a simple way to manage your tasks using CLI!
Available options:
'1' Print tasks
'2' Add a new task
'3' Edit an existing task
'4' Delete an existing task
'sq' - save and quit
'q' - quit
's' - save
'l' - load

> 2
To add new task you must fill these parameters:
ID - 1
Description - 2
Status - 3
To escape type 'q'
> 1
Input ID: 1
To add new task you must fill these parameters:
Description - 2
Status - 3
To escape type 'q'
> 2
Input Description: Complete the project
To add new task you must fill these parameters:
Status - 3
To escape type 'q'
> 3
Input Status: In progress
```

## Author

Created by TETROGAME - August 2025