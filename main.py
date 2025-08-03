from TaskTracker import *

def main() -> int:
    tasks = [Task(1, 'generic task')]
    tracker = TaskTracker(tasks)
    print(tracker)
    tracker.add_task()
    print(tracker)
    # tracker.update_task(task_id = 1)
    # print(tracker)
    return 0


if __name__ == '__main__':
    main()