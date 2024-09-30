from .keyword_exception import KeywordException

from getpass import getpass


class CoreFunctions:
    YES = 0,
    NO = 1,
    QUIT = 2,
    HELP = 3,
    PREV = 4,
    START = 5


class DataInput:
    def __init__(self, encoding: str):
        self.encoding: str = encoding


class KeywordDataInput(DataInput):
    def __init__(self, encoding, action):
        super().__init__(encoding)
        self.encoding = encoding
        self.action = action


class DataInputFactory:
    CORE_OPTIONS = {
        ':q': CoreFunctions.QUIT,
        ':quit': CoreFunctions.QUIT,
        ':h': CoreFunctions.HELP,
        ':help': CoreFunctions.HELP,
        ':p': CoreFunctions.PREV,
        ':prev': CoreFunctions.PREV,
        ':s': CoreFunctions.START,
        ':start': CoreFunctions.START
    }

    @staticmethod
    def create(msg: str, secret=False, create_stub=False) -> DataInput:
        if create_stub:
            return DataInput(None)
        if secret:
            option = getpass(msg)
        else:
            option = input(msg)

        if option in DataInputFactory.CORE_OPTIONS:
            raise KeywordException(DataInputFactory.CORE_OPTIONS[option])

        else:
            return DataInput(option)
