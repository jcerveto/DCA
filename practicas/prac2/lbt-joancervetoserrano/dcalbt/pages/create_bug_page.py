from .page import Page
from ..entry import DataInputFactory, CoreFunctions
from ..bug import BugCreator
from ..keyword_exception import KeywordException


class CreateBugPage(Page):
    CATEGORIES = {
        '0': 'RE-OPEN-REQUEST',
        '1': 'BUG',
        '2': 'ENHANCEMENT',
        '3': 'DOCUMENTATION',
        '4': 'DUPLICATE',
        '5': 'FEATURE-REQUEST',
        '6': 'OTHER',
    }

    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {

        }

    def show(self) -> str:
        return f'Rellena los siguientes campos para crear un nuevo issue.\n'

    def handle_input(self) -> None:
        title = DataInputFactory.create('Introduce el título: ')
        description = DataInputFactory.create('Introduce la descripción: ')

        category = DataInputFactory.create('Introduce la categoría: ')
        category.encoding = category.encoding.upper()
        while category.encoding not in self.CATEGORIES.values():
            category = DataInputFactory.create(f'ERROR: La categoría introducida no existe. '
                                               f'La categoría {category.encoding} no está en la lista: \n'
                                               f'{' '.join(self.CATEGORIES.values())}\n'
                                               f'Introduce la categoría: ')

        bug_creator = BugCreator.create(
            title=title.encoding,
            description=description.encoding,
            category=category.encoding,
            created_by=self.cli.session.username,
        )

        print(f'Estás a punto de crear el siguiente issue:'
              f'\n{bug_creator}\n')
        self.response = DataInputFactory.create('¿Quieres continuar? (S/n): ')
        if self.response.encoding.lower() == 'n':
            return None
        elif not self.response.encoding.lower() == 's':
            return None

        self.cli.storage.issues.append(bug_creator)

        print(f'Issue creado con el identificador #{bug_creator.bug_id}. ')
        self.press_enter_to_continue()
        raise KeywordException(CoreFunctions.START)
