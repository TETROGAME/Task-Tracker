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
                f'Updated at: {self._updatedAt}')
    def is_valid(self):
        pass


class TaskTracker:
    tasks: list[Task]
    def __init__(self, tasks: list[Task] = None):
        if tasks is None:
            tasks = []
        self.tasks = tasks
    def __repr__(self):
        return f'Stored tasks: {self.tasks}'

    def add_task(self, task: Task):
        if task.is_valid(): self.tasks.append(task)
        else: raise TaskError('Task is not valid')
        return self


def main() -> int:
    return 0


if __name__ == '__main__':
    main()