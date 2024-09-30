from ..entry import DataInput
from abc import ABC, abstractmethod
from enum import Enum

from ..entry import DataInputFactory


class Page(ABC):
    def __init__(self, cli: 'Cli'):
        self.cli = cli
        self.response: DataInput = None

    @abstractmethod
    def link_to_next_pages(self) -> dict:
        ...

    @abstractmethod
    def show(self) -> str:
        ...

    @abstractmethod
    def handle_input(self) -> None:
        ...

    def next_pages(self) -> list:
        return list(self.link_to_next_pages().values())

    def options(self) -> list:
        return list(self.link_to_next_pages().keys())

    def has_response(self):
        return self.response is not None

    def option_match(self):
        if not self.has_response():
            return False

        return (self.response.encoding in self.options()
                or self.response in DataInputFactory.CORE_OPTIONS)

    def press_enter_to_continue(self):
        self.response = DataInputFactory.create('Pulsa ENTER para continuar...')

    def __str__(self):
        return f'({self.__class__.__name__})'
