from enum import Enum
from .communication import Communication
from datetime import datetime


class BugCategory(Enum):
    Important = 'important'
    Normal = 'normal'
    Minor = 'minor'
    Wishlist = 'wishlist'


class BugStatus(Enum):
    Open = 0
    Closed = 1

    def __lt__(self, other):
        return self.value < other.value


class Role(Enum):
    Admin = 'admin'
    User = 'user'


class Bug:
    def __init__(
            self,
            bug_id: int,
            title: str,
            description: str,
            category: str,
            created_by: str
    ):
        self.bug_id = bug_id
        self.title = title
        self.description = description
        self.category = category
        self.created_by = created_by
        self._status = BugStatus.Open
        self.communications = []
        self.times_opened = 1
        self.date = datetime.now()

    def full_info(self) -> str:
        return f'{self}{self.thread()}'

    def small_info(self) -> str:
        return f'#{self.bug_id}\t {self.title}'

    def thread(self) -> str:
        if len(self.communications) == 0:
            return '\n\tEste issue no tiene ninguna comunicación asociada.'

        thread_info = [f'\t[{i + 1}] {str(c)}' for i, c in enumerate(self.communications)]
        return f'\n\tMostrando {len(self.communications)} comunicación/es:\n' + '\n'.join(thread_info)

    def __str__(self):
        return (f'#{self.bug_id} '
                f'[{self.category}] '
                f'{self.title.upper()}: '
                f'{self.description.capitalize()} '
                f' (por {self.created_by}) [{self.date.strftime("%d/%m/%Y %H:%M:%S")}] '
                f'Estado: {'ABIERTO' if self.status == BugStatus.Open else 'CERRADO'}'
                f' {len(self.participants())} participants.'
                f' {self.times_closed()} veces cerrado. {self.times_opened} veces abierto.')

    def times_closed(self) -> int:
        return self.times_opened - 1

    def times_opened(self) -> int:
        return self.times_opened

    def add_communication(self, communication: Communication):
        self.communications.append(communication)
        return self

    def participants(self) -> list:
        return [c.username for c in self.communications] + [self.created_by]

    @property
    def status(self) -> BugStatus:
        return self._status

    @status.setter
    def status(self, status: BugStatus):
        if self._status == BugStatus.Closed and status == BugStatus.Open:
            self.times_opened += 1

        self._status = status


class BugCreator:
    NEXT_ID = 1

    @classmethod
    def create(cls, title: str, description: str, category: str, created_by: str):
        new_id = cls.NEXT_ID
        cls.NEXT_ID += 1

        return Bug(
            bug_id=new_id,
            title=title,
            description=description,
            category=category,
            created_by=created_by,
        )
