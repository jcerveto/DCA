from .page import Page
from ..entry import DataInputFactory, CoreFunctions
from ..bug import Bug, BugStatus
from ..communication import Communication
from datetime import datetime

from ..keyword_exception import KeywordException


class OpenCloseIssuePage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {}

    def show(self) -> str:
        return (f'¿Abrir o cerrar un issue?\n'
                f'Podrás cerrar issues abiertos o abrir issues cerrados. \n')

    def handle_input(self) -> None:
        try:
            print(f'Se mostrarán los issues en memoria: ')
            for issue in self.cli.storage.issues:
                print(issue.small_info())
            if len(self.cli.storage.issues) == 0:
                print('No hay issues para mostrar.\n')
            self.response = DataInputFactory.create('Introduce el identificador del issue: ')
            self.response.encoding.replace(' ', '').replace('#', '')

            issue_reference: Bug = \
                self.cli.storage.filter_issues_by_option(category='id', value=self.response.encoding)[0]
            print(f'El issue seleccionado se encuentra en estado '
                  f'{"ABIERTO" if issue_reference.status == BugStatus.Open else "CERRADO"}\n'
                  f'Información del issue: \n{issue_reference.full_info()}\n')

            self.action = DataInputFactory.create('¿Abrir o cerrar el issue? (Abrir/Cerrar): ')
            while self.action.encoding.upper() not in {'ABRIR', 'CERRAR'}:
                print('Por favor, introduce un valor correcto (Abrir/Cerrar): ')
                self.action = DataInputFactory.create('¿Abrir o cerrar el issue? (Abrir/Cerrar): ')

            valid_action = BugStatus.Open if self.action.encoding.upper() == 'ABRIR' else BugStatus.Closed
            if issue_reference.status == valid_action:
                print(f'El issue ya se encuentra en estado '
                      f'{"ABIERTO" if issue_reference.status == BugStatus.Open else "CERRADO"}')
                self.press_enter_to_continue()
                return None

            self.action = DataInputFactory.create(f'¿Seguro que deseas '
                                                  f'{"Abrir" if valid_action == BugStatus.Open else "Cerrar"}'
                                                  f' el issue? (S/n): ')
            self.action.encoding.upper()
            while self.action.encoding.upper() not in {'S', 'N'}:
                print('Por favor, introduce un valor correcto (S/n): ')
                self.action = DataInputFactory.create(f'¿Seguro que deseas '
                                                      f'{"Abrir" if valid_action == BugStatus.Open else "Cerrar"}'
                                                      f' el issue? (S/n): ')
            if self.action.encoding.upper() == 'N':
                print(f'Operación cancelada.')
                self.press_enter_to_continue()
                return None

            if self.action.encoding.upper() == 'ABRIR':
                issue_reference.status = BugStatus.Open
                issue_reference.add_communication(
                    Communication(
                        title='Issue abierto',
                        description=(f'El issue abierto a las {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} '
                                     f'por el/la usuario/a {self.cli.session.username} '
                                     f'por {issue_reference.times_opened + 1} vez/veces.\n'),
                        username=self.cli.session.username
                    )
                )
            else:
                issue_reference.status = BugStatus.Closed
                issue_reference.add_communication(
                    Communication(
                        title='Issue cerrado',
                        description=(f'El issue cerrado a las {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} '
                                     f'por el/la usuario/a {self.cli.session.username} '
                                     f'por {issue_reference.times_closed() + 1} vez/veces.\n'),
                        username=self.cli.session.username
                    )
                )
            print(f'El issue ha sido {"abierto" if issue_reference.status == BugStatus.Open else "cerrado"}')
            self.press_enter_to_continue()

            raise KeywordException(CoreFunctions.PREV)

        except IndexError as e:
            print(f'No se ha encontrado ningún issue con ese identificador. (#{self.response.encoding})')
