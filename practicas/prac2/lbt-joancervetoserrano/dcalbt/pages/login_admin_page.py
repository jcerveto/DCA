from .page import Page
from ..entry import DataInputFactory
from .admin_menu_options_page import AdminMenuOptionsPage
from ..session import Session
from ..bug import Role


class LoginAdminPage(Page):
    admins = [
        ('admin', 'admin'),
        ('admin', 'adminadmin'),
        ('admin', '1234'),
        ('admin', 'admin1234'),
        ('admin', '0000'),
    ]

    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '*': AdminMenuOptionsPage
        }

    def show(self) -> str:
        content = (f'Introduce tus datos para que tu comunicación quede registrada.\n'
                   f'Valida tu usuario y contraseña para comprobar que tienes permisos de administrador. \n')

        return content

    def handle_input(self):
        self.username = DataInputFactory.create('Introduce tu nombre de usuario: ')
        self.password = DataInputFactory.create('Introduce tu contraseña: ', secret=True)

        if (self.username.encoding, self.password.encoding) not in self.admins:
            print('ERROR: Credenciales incorrectas. '
                  'Por favor, introduce tus credenciales de administrador. ')
            return None

        self.cli.session = Session(self.username.encoding, Role.Admin.value)

        return self.link_to_next_pages()['*'](self.cli)
