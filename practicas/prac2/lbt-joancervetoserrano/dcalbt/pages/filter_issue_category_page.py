from .page import Page
from ..entry import DataInputFactory
from .create_bug_page import CreateBugPage


class FilterIssuesByCategoryPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '1': 'id',
            '2': 'title',
            '3': 'description',
            '4': 'category',
            '5': 'status',
            '6': 'created_by',
            '7': 'participant',
            '8': 'participant',
        }

    def show(self) -> str:
        return (f'Filtrar por categoría: \n'
                f'1. Identificador. \n'
                f'2. Título. \n'
                f'3. Descripción. \n'
                f'4. Categoría. \n'
                f'5. Estado. \n'
                f'6. Creador/a. \n'
                f'7. Participante. \n'
                f'8. Sobre ti. \n')

    def handle_input(self) -> None:
        self.response = DataInputFactory.create('Selecciona una opción: ')

        if self.response.encoding not in self.options():
            return None
        if self.response.encoding == '8':
            self.filter_value = DataInputFactory.create(None, create_stub=True)
            self.filter_value.encoding = self.cli.session.username
        else:
            self.filter_value = DataInputFactory.create('Introduce el valor a filtrar: ')

        if self.response.encoding == '4' and self.filter_value.encoding.upper() not in CreateBugPage.CATEGORIES.values():
            print('ERROR: El valor a filtrar no se encuentra en la lista de categorías.\n'
                  'Tiene que estar en la lista de categorías: \n'
                  f'{" ".join(CreateBugPage.CATEGORIES.values())}')
            self.filter_value = DataInputFactory.create('Introduce el valor a filtrar: ')
        self.filter_value.encoding = self.filter_value.encoding.upper()


        if self.response.encoding.upper() == '5' and self.filter_value.encoding.upper() not in {'OPEN', 'CLOSED'}:
            print('ERROR: El valor a filtrar no se encuentra en la lista de estados.\n'
                  'Tiene que estar en la lista de estados: \n'
                  f'{" ".join({'OPEN', 'CLOSED'})}')
            self.filter_value = DataInputFactory.create('Introduce el valor a filtrar: ')

        if self.response.encoding.upper() == '5':
            if self.filter_value.encoding.upper() == 'OPEN':
                self.filter_value.encoding = 0
            else:
                self.filter_value.encoding = 1

        show_all = DataInputFactory.create('¿Mostrar la información detallada de cada issue? (S/n): ')
        while show_all.encoding.lower() not in {'s', 'n'}:
            show_all = DataInputFactory.create('ERROR: La respuesta debe ser S, s, o N, n. '
                                               '¿Mostrar la información detallada de cada issue? (S/n): ')

        self.show_content(show_all=show_all.encoding.lower() == 's')

        self.press_enter_to_continue()
        return 0

    def show_content(self, show_all: bool) -> None:
        content = f'Listando issues por {self.link_to_next_pages()[self.response.encoding]}...\n'
        issues = self.cli.storage.filter_issues_by_option(
            category=self.link_to_next_pages()[self.response.encoding],
            value=self.filter_value.encoding)

        for issue in issues:
            if show_all:
                content += f'{issue.full_info()}\n'
            else:
                content += f'{issue}\n'
        if len(issues) == 0:
            content += 'No hay issues para mostrar.\n'

        print(content)
