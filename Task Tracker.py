from datetime import datetime

status_list = ('In progress', 'Done')
class Task:
    _id: int
    _description: str
    _status: str
    _cratedAt: datetime
    _updatedAt: datetime
    def __init__(self, _id: int = 0, _description: str = '', _status: str = status_list[0]
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

def main() -> int:
    return 0




if __name__ == '__main__':
    main()