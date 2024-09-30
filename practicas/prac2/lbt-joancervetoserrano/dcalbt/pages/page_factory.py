from enum import Enum

from .start_page import StartPage
from .login_client_page import LoginClientPage
from .login_admin_page import LoginAdminPage
from .last_page import LastPage


class PageFactoryOptions(Enum):
    START = 'start'
    LOGIN_CLIENT = 'login_client'
    LOGIN_ADMIN = 'login_admin'
    LAST_PAGE = 'last'


class PageFactory:
    @classmethod
    def create(cls, option, cli: 'Cli'):
        if option == PageFactoryOptions.START:
            return StartPage(cli)
        if option == PageFactoryOptions.LOGIN_CLIENT:
            return LoginClientPage(cli)
        if option == PageFactoryOptions.LOGIN_ADMIN:
            return LoginAdminPage(cli)
        if option == PageFactoryOptions.LAST_PAGE:
            return LastPage(cli)

        raise ValueError(f'Invalid option for PageFactory. Valid options are {list(PageFactoryOptions)}')
