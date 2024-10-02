from .page import Page
from ..entry import DataInputFactory, CoreFunctions
from ..bug import Bug, BugStatus
from ..communication import Communication
from ..keyword_exception import KeywordException


class CreateCommunicationPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {}

    def show(self) -> str:
        return (f'Añade una mensaje a un issue.\n'
                f'Cada issue tendrá un hilo de comunicaciones donde todos los usarios pueden intervenir. \n'
                f'Los clientes expondrán sus dudas o comentarios y '
                f'los administradores se encargarán de la gestión de los mismos. \n\n'
                f'Solo los administradores podrán abrir o cerrar  issues. Pero los clientes pueden abrir un nuevo issue'
                f'con la categoría "RE-OPEN-REQUEST" para solicitar abrir de nuevo el hilo de un issue.\n')

    def handle_input(self) -> None:
        bug_id = None
        try:
            self.response = DataInputFactory.create('Introduce el identificador del issue: ')
            bug_id = int(self.response.encoding.replace('#', '').replace(' ', ''))
            bug_reference: Bug = self.cli.storage.filter_issues_by_option(category='id', value=bug_id)[0]

            print(f'Mostrando información del issue actual: \n'
                  f'{bug_reference.full_info()}')

            if bug_reference.status != BugStatus.Open:
                print(f'El issue seleccionado no se encuentra abierto. No se puede anadir una comunicación. '
                      f'Crea un nuevo issue con la categoría "RE-OPEN-REQUEST" para solicitar abrir de nuevo el hilo de este issue.'
                      f' con identificador #{bug_reference.bug_id}. ')
                self.press_enter_to_continue()
                raise KeywordException(CoreFunctions.START)

            print(f'Se mostrarán los issues en memoria: ')
            for issue in self.cli.storage.issues:
                print(issue.small_info())
            if len(self.cli.storage.issues) == 0:
                print('No hay issues para mostrar.\n')

            title = DataInputFactory.create('Introduce el título de tu comunicación: ')
            description = DataInputFactory.create('Introduce la descripción de tu comunicación: ')

            new_communication = Communication(
                title=title.encoding.title(),
                description=description.encoding.capitalize(),
                username=self.cli.session.username.capitalize(),
            )

            bug_reference.add_communication(new_communication)

            print(f'La comunicación se ha añadido al hilo del bug #{bug_reference.bug_id}. ')
            self.press_enter_to_continue()
            raise KeywordException(CoreFunctions.START)
        except ValueError:
            print(f'No se ha encontrado un bug con ese identificador. (#{bug_id})')
            return None
        except IndexError:
            print(f'El identificador {bug_id} no se encuentra en la lista de issues.')
            return None
