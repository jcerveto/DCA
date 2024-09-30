from .page import Page
from ..entry import DataInputFactory
from ..session import Session
from ..bug import Role
from .client_menu_options_page import ClientMenuOptionsPage


class LoginClientPage(Page):

    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '*': ClientMenuOptionsPage,
        }

    def show(self) -> str:
        content = f'Introduce tus datos para que tu comunicación quede registrada.\n'

        return content

    def handle_input(self) -> None:
        self.response = DataInputFactory.create('Introduce tu nombre de usuario: ')
        self.cli.session = Session(self.response.encoding, Role.User.value)

        print(f'Welcome {self.response.encoding}!')

        return self.link_to_next_pages()['*'](self.cli)
