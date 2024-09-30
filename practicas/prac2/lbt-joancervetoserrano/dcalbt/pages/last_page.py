from .page import Page


class LastPage(Page):
    def __init__(self, cli: 'Cli'):
        super().__init__(cli)

    def link_to_next_pages(self) -> dict:
        return {}

    def show(self) -> str:
        content = f'Cerrando sesión...\n'

        return content

    def handle_input(self) -> None:
        pass
