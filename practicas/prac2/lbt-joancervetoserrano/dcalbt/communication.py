from datetime import datetime


class Communication:
    def __init__(
            self,
            title: str,
            description: str,
            username: str,
    ):
        self.title = title
        self.description = description
        self.username = username
        self.date = datetime.now()

    def __str__(self):
        return f'[{self.username}] {self.title.upper()}: {self.description}'

