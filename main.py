from TaskTracker import *

def main() -> int:
    print('Welcome to Task Tracker, a simple way to manage your tasks using CLI!')
    while True:
        print('Available options:\n'
              '1. Print existing tasks\n'
              '2. Add a new task\n'
              '3. Edit an existing task\n'
              '4. Delete an existing task\n'
              '5. Exit\n\n'
              'To quit without saving type \'q\'\n'
              'To save and quit type \'sq\'\n'
              'To save type \'s\'\n'
              'To load type \'l\'\n')
        user_input = input('> ')
        match user_input:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case 'q':
                pass
            case 'sq':
                pass
            case 's':
                pass
            case 'l':
                pass
            case _:
                print('Invalid input. Please try again.')
                break
    return 0


if __name__ == '__main__':
    main()