from os import system, name
from .pages import Page
from .session import Session
from .entry import CoreFunctions

class View:
    ROW = 80 * '*'

    def __init__(
            self,
            current_page: Page,
            iteration,
    ):
        self.current_page = current_page
        self.iteration = iteration

    def has_next_pages(self):
        return self.current_page.next_pages() is not None and len(self.current_page.next_pages()) > 0

    def show(self, session: Session, ignore_clear=False) -> None:
        if not ignore_clear:
            self.clear()
        content = self.header(session)
        content += self.current_page.show()
        content += self.footer()

        print(content)

    def header(self, session) -> str:
        content = (f'{self.ROW}\n'
                   f'Local Bug Tracker\t\tDCA\t\t2024\t\tLBTua\n'
                   f'{f'[{session.role}] {session.username}\n' if session is not None else '[Sin registro]'}\n'
                   f'{self.ROW}\n')

        return content

    def footer(self) -> str:
        content = (f'{self.ROW}\n'
                   f'iteration: {self.iteration}\t\tpage: {self.current_page.__class__.__name__}\t\t'
                   f'[:q :quit :p :prev :s :start]\n'
                   f'{self.ROW}')

        return content

    @classmethod
    def clear(cls) -> None:
        print("\n" * 30)
        # for windows
        # if name == 'nt':
        #    _ = system('cls')
        #
        # for mac and linux(here, os.name is 'posix')
        # else:
        #    print('Clearing...')
        #    _ = system('clear')
        #    print('It is clear now')

    def __str__(self):
        return f'(V{str(self.current_page)})'
