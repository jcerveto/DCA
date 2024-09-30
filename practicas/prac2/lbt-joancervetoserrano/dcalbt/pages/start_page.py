from .page import Page
from .login_admin_page import LoginAdminPage
from .login_client_page import LoginClientPage
from ..entry import DataInputFactory


class StartPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '1': LoginClientPage,
            '2': LoginAdminPage
        }

    def show(self) -> str:
        content = (f'¡Te damos la bienvenida a Local Bug Tracker!\n'
                   f'Selecciona una opción para comenzar:\n'
                   f'1. Soy un/a cliente/a que quiere añadir una comunicación. \n'
                   f'2. Soy un/a administrador/a. \n')

        return content

    def handle_input(self) -> Page | None:
        self.response = DataInputFactory.create('Selecciona una opción: ')
        if self.response.encoding not in self.options():
            print('Input should be in: ', self.options(), sep='')
            return None

        return self.link_to_next_pages()[self.response.encoding](self.cli)



