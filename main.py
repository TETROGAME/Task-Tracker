from TaskTracker import *
def main() -> int:
    tracker = TaskTracker()
    print('Welcome to Task Tracker, a simple way to manage your tasks using CLI!')
    while True:
        print('Available options:\n'
              '\'1\' Print existing tasks\n'
              '\'2\' Add a new task\n'
              '\'3\' Edit an existing task\n'
              '\'4\' Delete an existing task\n'
              '\'5\' Exit\n'
              '\'sq\' - save and quit\n'
              '\'q\' - quit\n'
              '\'s\' - save\n'
              '\'l\' - load\n')

        user_input = input('> ')
        match user_input:
            case '1':
                if tracker.get_tasks():
                    print(f'Tasks list:\n{tracker}\n')
                else:
                    print('No tasks saved\n')
            case '2':
                tracker.add_task()
            case '3':
                user_input = input('Enter task ID: ')
                try:
                    tracker.update_task(int(user_input))
                except ValueError as error:
                    print(error)
            case '4':
                pass
            case '5':
                pass
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