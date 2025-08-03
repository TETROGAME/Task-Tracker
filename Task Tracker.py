from datetime import datetime

STATUS_LIST = ('In progress', 'Done')

class TaskError(Exception):
    def __init__(self, message):
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

    def set_description(self, description: str):
        self._description = description

    def set_status(self, status: str):
        self._status = status

    def set_cratedAt(self, cratedAt: datetime):
        self._cratedAt = cratedAt

    def set_updatedAt(self, updatedAt: datetime):
        self._updatedAt = updatedAt

    def is_valid(self):
        return True



class TaskTracker:
    tasks: list[Task]
    def __init__(self, tasks: list[Task] = None):
        if tasks is None:
            tasks = []
        for task in tasks:
            if not isinstance(task, Task):
                raise ValueError(f'Element at {tasks.index(task)} position is not an instance of Task class')
        self.tasks = tasks
    def __repr__(self):
        result = ''
        for i, task in enumerate(self.tasks):
            result += f'Task #{i+1}: {task}'
        return result

    def add_task(self, task: Task):
        if task.is_valid():
            self.tasks.append(task)
        else:
            raise TaskError('Task is not valid')
        return self
    def update_task(self, task_id: int):
        target_task = next((task for task in self.tasks if task.get_id() == task_id), None)
        if target_task:
            while True:
                print('Select parameter to update:\n'
                      'Description - 1\n'
                      'Status - 2\n'
                      'To exit type \'q\'')
                user_input = input(':')
                match user_input:
                    case '1':
                        try:
                            new_description = input('Input new description for task: ')
                            if new_description:
                                target_task.set_description(new_description)
                            else:
                                raise TaskError('Task description can not be empty')
                        except TaskError as error:
                            print(f'Error message: {error}')
                    case '2':
                        try:
                            new_status = input('Input new status for task: ')
                            if new_status in STATUS_LIST:
                                target_task.set_status(new_status)
                            else:
                                raise TaskError('Status must be a value from STATUS_LIST:\n'
                                                f'{STATUS_LIST}')
                        except TaskError as error:
                            print(f'Error message: {error}')
                    case 'q':
                        print(f'Done updating task {target_task.get_id()}')
                        break
                    case _:
                        print('Invalid input')
        else: print('No task to update')


def main() -> int:
    return 0


if __name__ == '__main__':
    main()