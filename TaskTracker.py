from datetime import datetime

STATUS_LIST = ('New', 'In progress', 'Done')

class TaskError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class Task:
    _id: int
    _description: str
    _status: str
    _cratedAt: datetime
    _updatedAt: datetime
    def __init__(self, _id: int = 0, _description: str = '', _status: str = STATUS_LIST[0]
                 , _cratedAt: datetime = datetime.date(datetime.now())
                 , _updatedAt: datetime = datetime.date(datetime.now())):
        self._id = _id
        self._description = _description
        self._status = _status
        self._cratedAt = _cratedAt
        self._updatedAt = _updatedAt
    def __repr__(self):
        return (f'ID: {self._id}\nDescription: {self._description}\n'
                f'Status: {self._status}\nCreated at: {self._cratedAt}\n'
                f'Updated at: {self._updatedAt}\n')

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_status(self):
        return self._status

    def get_cratedAt(self):
        return self._cratedAt

    def get_updatedAt(self):
        return self._updatedAt

    def set_id(self, _id: int):
        self._id = _id
    def set_description(self, description: str) -> bool:
        try:
            if description:
                self._description = description
                return True
            else:
                raise TaskError('Description cannot be empty')
        except TaskError as error:
            print(f'TaskError: {error}')
            return False

    def set_status(self, status: str) -> bool:
        try:
            if status in STATUS_LIST:
                self._status = status
                return True
            else:
                raise TaskError('Status must be value from STATUS_LIST')
        except TaskError as error:
            print(f'TaskError: {error}')
            return False

    def set_cratedAt(self, cratedAt: datetime):
        self._cratedAt = cratedAt

    def set_updatedAt(self, updatedAt: datetime):
        self._updatedAt = updatedAt

    # def is_valid(self):
    #     return True

class TaskTracker:
    _tasks: list[Task]
    def __init__(self, tasks: list[Task] = None):
        if tasks is None:
            tasks = []
        for task in tasks:
            if not isinstance(task, Task):
                raise ValueError(f'Element at {tasks.index(task)} position is not an instance of Task class')
        self._tasks = tasks
    def __repr__(self):
        result = ''
        for i, task in enumerate(self._tasks):
            result += f'Task #{i+1}: {task}'
        return result
    def add_task(self, task: Task = None):
        if task is None:
            id_done = False
            description_done = False
            status_done = False

            new_task = Task()

            while not id_done or not description_done or not status_done:
                print('To add new task you must fill these parameters:')
                if not id_done: print('ID - 1')
                if not description_done: print('Description - 2')
                if not status_done: print('Status - 3')
                user_input = input(':')
                match user_input:
                    case '1':
                        try:
                            new_task.set_id(int(input('Input ID: ')))
                            id_done = True
                        except ValueError:
                            print('ID must be positive integer')
                            pass
                    case '2':
                        if new_task.set_description(input('Input Description: ')):
                            description_done = True
                        else:
                            pass
                    case '3':
                        if new_task.set_status(input('Input Status: ')):
                            status_done = True
                        else:
                            pass
                    case _:
                        print('Invalid input')
            self._tasks.append(new_task)
        else:
            self._tasks.append(task)

    def update_task(self, task_id: int):
        target_task = next((task for task in self._tasks if task.get_id() == task_id), None)
        if target_task:
            while True:
                print('Select parameter to update:\n'
                      'Description - 1\n'
                      'Status - 2\n'
                      'To exit type \'q\'')
                user_input = input(':')
                match user_input:
                    case '1':
                        new_description = input('Input new description for task: ')
                        target_task.set_description(new_description)
                    case '2':
                        new_status = input('Input new status for task: ')
                        target_task.set_status(new_status)
                    case 'q':
                        print(f'Done updating task with id: {target_task.get_id()}')
                        break
                    case _:
                        print('Invalid input')
        else: print('No task to update')


