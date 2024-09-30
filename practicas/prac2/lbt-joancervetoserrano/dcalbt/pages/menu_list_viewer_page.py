from .page import Page
from ..entry import DataInputFactory
from .filter_issue_category_page import FilterIssuesByCategoryPage
from .sort_issue_category_page import SortIssuesByCategoryPage


class MenuListViewerPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)


    def link_to_next_pages(self) -> dict:
        return {
            '1': SortIssuesByCategoryPage,
            '2': FilterIssuesByCategoryPage,
        }

    def show(self) -> str:
        return (f'Selecciona cómo quieres ver los issues: \n'
                f'1. Ordenados por categoría (ver todos los issues). \n'
                f'2. Filtrados por categoría (ver únicamente algunos issues). \n')

    def handle_input(self) -> None:
        self.response = DataInputFactory.create('Selecciona una opción: ')

        if self.response.encoding not in self.options():
            return None

        return self.link_to_next_pages()[self.response.encoding](self.cli)
