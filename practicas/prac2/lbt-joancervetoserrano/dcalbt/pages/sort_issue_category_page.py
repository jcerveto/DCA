from .page import Page
from ..entry import DataInputFactory


class SortIssuesByCategoryPage(Page):
    def __init__(self, cli):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {
            '1': 'id',
            '2': 'title',
            '3': 'description',
            '4': 'category',
            '5': 'status',
            '6': 'date',
            '7': 'created_by',
        }

    def show(self) -> str:
        return (f'Ordenar por categoría: \n'
                f'1. Identificador. \n'
                f'2. Título. \n'
                f'3. Descripción. \n'
                f'4. Categoría. \n'
                f'5. Estado. \n'
                f'6. Fecha. \n'
                f'7. Creador/a. \n')

    def handle_input(self) -> None:
        self.response = DataInputFactory.create('Selecciona una opción: ')

        if self.response.encoding not in self.options():
            return None

        show_all = DataInputFactory.create('¿Mostrar la información detallada de cada issue? (S/n): ')
        while show_all.encoding.lower() not in {'s', 'n'}:
            show_all = DataInputFactory.create('ERROR: La respuesta debe ser S, s, o N, n. '
                                               '¿Mostrar la información detallada de cada issue? (S/n): ')

        self.show_content(show_all=show_all.encoding.lower() == 's')
        self.press_enter_to_continue()
        return 0

    def show_content(self, show_all: bool) -> None:
        content = f'Listando issues por ${self.response.encoding}...\n'
        issues = self.cli.storage.sort_issues_by_option(self.link_to_next_pages()[self.response.encoding])

        for issue in issues:
            if show_all:
                content += f'{issue.full_info()}\n'
            else:
                content += f'{issue}\n'
        if len(issues) == 0:
            content += 'No hay issues para mostrar.\n'

        print(content)
