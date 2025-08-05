from TaskTracker import *

def print_tasks(tracker: TaskTracker) -> None:
    if tracker.get_tasks():
        print('Select print options:\n'
          '\'1\' Print all existing tasks\n'
          '\'2\' Print all done tasks\n'
          '\'3\' Print all in progress tasks\n'
          '\'4\' Print all not done tasks')
        match input('> '):
            case '1':
                print(f'Tasks list:\n{tracker}\n')
            case '2':
                if tracker.get_done_tasks():
                    print('Done tasks list:')
                    for task in tracker.get_done_tasks():
                        print(task)
                else:
                    print('No tasks with status \'done\'')
            case '3':
                if tracker.get_in_progress_tasks():
                    print('In progress tasks list:')
                    for task in tracker.get_in_progress_tasks():
                        print(task)
                else:
                    print('No tasks with status \'in progress\'')
            case '4':
                if tracker.get_not_done_tasks():
                    print('Not done tasks:')
                    for task in tracker.get_not_done_tasks():
                        print(task)
                else:
                    print('No tasks with status not \'done\'')
            case _:
                print('Invalid input')
    else:
        print('No tasks saved\n')

def validate_task_id(func):
    def wrapper(tracker):
        user_input = input('Enter task ID: ')
        try:
            task_id = int(user_input)
            return func(tracker, task_id)
        except ValueError as error:
            print(f"Invalid task ID: {error}")
            return False
    return wrapper

@validate_task_id
def update_task_option(tracker: TaskTracker, task_id: int):
    tracker.update_task(task_id)

@validate_task_id
def delete_task_option(tracker: TaskTracker, task_id: int):
    tracker.delete_task(task_id)

def main() -> int:
    tracker = TaskTracker()
    print('Welcome to Task Tracker, a simple way to manage your tasks using CLI!')
    while True:
        print('Available options:\n'
              '\'1\' Print tasks\n'
              '\'2\' Add a new task\n'
              '\'3\' Edit an existing task\n'
              '\'4\' Delete an existing task\n'
              '\'sq\' - save and quit\n'
              '\'q\' - quit\n'
              '\'s\' - save\n'
              '\'l\' - load\n')

        user_input = input('> ')
        match user_input:
            case '1':
                print_tasks(tracker)
            case '2':
                tracker.add_task()
            case '3':
                update_task_option(tracker)
            case '4':
                delete_task_option(tracker)
            case 'q':
                print('Quitting...')
                exit(0)
            case 'sq':
                tracker.save()
                print('Quitting...')
                break
            case 's':
                tracker.save()
            case 'l':
                tracker.load()
            case _:
                print('Invalid input. Please try again.')
    return 0


if __name__ == '__main__':
    main()