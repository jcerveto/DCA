from .page import Page
from ..entry import DataInputFactory
from ..session import Session
from ..bug import Role
from .menu_list_viewer_page import MenuListViewerPage
from .create_bug_page import CreateBugPage
from .create_communication_page import CreateCommunicationPage
from .open_close_issue_page import OpenCloseIssuePage


class AdminMenuOptionsPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '1': MenuListViewerPage,
            '2': CreateBugPage,
            '3': CreateCommunicationPage,
            '4': OpenCloseIssuePage
        }

    def show(self) -> str:
        content = (f'¿Qué opción deseas realizar?.\n'
                   f'1. Ver todos los issues.\n'
                   f'2. Crear un nuevo issue.\n'
                   f'3. Añadir una nueva comunicación a un issue.\n'
                   f'4. Reabrir o cerrar un issue.\n')

        return content

    def handle_input(self) -> None:
        self.response = DataInputFactory.create('Selecciona una opción: ')

        if self.response.encoding not in self.options():
            return None

        return self.link_to_next_pages()[self.response.encoding](self.cli)

