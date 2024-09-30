from sys import stderr

from .pages import PageFactory, PageFactoryOptions, Page, DataInputFactory
from .view import View
from .storage import Storage
from .keyword_exception import KeywordException
from .entry import CoreFunctions


class Cli:
    def __init__(self):
        self.views = []
        self.storage = Storage()
        self._create()


    def _create(self):
        self.iteration = 0
        self.views = [View(PageFactory.create(PageFactoryOptions.START, self), self.iteration)]
        self.last_view = None
        self.session = None
        self.error = False
        self.ignore_clear = False
        self.iteration = 0

    def main_loop(self):
        while True:
            self._create()
            self.start_session()

    def start_session(self):
        try:
            # Iteramos todas las vistas hasta que no existan más páginas
            while len(self.views) > 0:
                try:
                    print(f'Issues in storage: {len(self.storage.issues)}')
                    self.views[-1].show(self.session, ignore_clear=self.ignore_clear)
                    self.error = False
                    next_page = self.handle_new_view()
                    if next_page is None:
                        self.views.pop()
                    else:
                        self.views.append(View(next_page, self.iteration + 1))
                except KeywordException as e:
                    if e.keyword == CoreFunctions.QUIT:
                        print('Bye bye!')
                        exit(0)
                    elif e.keyword == CoreFunctions.HELP:
                        print(f'En cualquier momento puedes pulsar las combinaciones de telcas reservadas: \n'
                              f'\t - :h o :help para mostrar un mensaje de ayuda.\n'
                              f'\t - :s o :start para iniciar una nueva sesión.\n'
                              f'\t - :p o :prev para retroceder una página.\n'
                              f'\t - :q o :quit para cerrar el programa.\n')
                        self.ignore_clear = True
                    elif e.keyword == CoreFunctions.PREV:
                        if len(self.views) > 1:
                            self.views.pop()
                    elif e.keyword == CoreFunctions.START:
                        self._create()
                    else:
                        print('Re-raising exception')
                        raise e

        except KeyboardInterrupt:
            print('\n\n\nBye bye!')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            self.show_last_view()

    def is_active_session(self):
        return self.session is not None

    def show_error_message(self):
        if self.error:
            print('Opción inválida. Por favor, introduce un valor correcto.\n', flush=True)

    def show_last_view(self):
        self.views.append(View(PageFactory.create(PageFactoryOptions.LAST_PAGE, self), self.iteration + 1))
        self.views[-1].show(self.session, ignore_clear=True)

    def handle_new_view(self):
        self.error = False
        while True:
            self.views[-1].show(self.session, ignore_clear=self.ignore_clear)
            self.show_error_message()
            self.ignore_clear = False

            next_page = self.views[-1].current_page.handle_input()
            if next_page is None:
                self.error = True
                continue
            if next_page == 0:
                self.error = False
                self.ignore_clear = True
                continue
            if isinstance(next_page, Page):
                return next_page
            else:
                raise ValueError('Page has not been instantiated correctly')