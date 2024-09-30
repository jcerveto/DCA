from .bug import BugCreator
from .communication import Communication


class Storage:
    def __init__(self, create_migrations=True):
        self.issues = []

        if create_migrations:
            more_issues = [
                BugCreator.create(
                    title='Se queda colgado al cargar el móvil'.title(),
                    description='No puedo registrar el usuario cuando estoy conectado a la corriente!!'.capitalize(),
                    category='BUG',
                    created_by='Joan'
                ).add_communication(
                    Communication(
                        title='¿Has probado a reiniciar?'.title(),
                        description='En mi teléfono funciona. Seguramente si reinciar el dispositivo funcionará...'.capitalize(),
                        username='admin'
                    )
                ),
                BugCreator.create(
                    title='Botón de cerrar sesión raro'.title(),
                    description='Cuando le doy a cerrar sesión sigo viendo mi foto de perfil aunque debería de estar la sesión cerrada...'.capitalize(),
                    category='BUG',
                    created_by='Joan'
                ).add_communication(
                    Communication(
                        title='Estamos trabajando en ello'.title(),
                        description='Seguramente para el lunes que viene esté resuelta esta incidencia. '.capitalize(),
                        username='admin'
                    )
                ),
                BugCreator.create(
                    title='No puedo borrar un usuario'.title(),
                    description='No se puede borrar un usuario que ya se había borrado previamente y se ha vuelto a crear'.capitalize(),
                    category='ENHANCEMENT',
                    created_by='Marc'
                ),
                BugCreator.create(
                    title='Nou idioma, valencià'.title(),
                    description='Vull distribuir el software a Andorra però necessite que introduiu el valencià a l\'aplicació. '.capitalize(),
                    category='FEATURE-REQUEST',
                    created_by='Marc'
                ),
                BugCreator.create(
                    title='NO ENTIENDO NADA!!'.title(),
                    description='Quiero añadir una nueva funcionalidad al módulo de autentificación para mejorar'
                                ' el tratamiento de usuarios pero no entiendo el código. '
                                '¿Podéis añadir documentación al código fuente?'.capitalize(),
                    category='DOCUMENTATION',
                    created_by='Aïna'
                ).add_communication(
                    Communication(
                        title='¿En qué formato prefieres la documentación?'.title(),
                        description='En python hay diferentes modelos de documentación: el estándar de '
                                    'Google, de LaTeX, etc. Coméntanos en qué formato lo prefieres. '.capitalize(),
                        username='admin'
                    )
                ),
                BugCreator.create(
                    title='Presupuesto $$$$'.title(),
                    description='Estoy interesada en adquirir una aplicación como la vuestra pero que tenga también una '
                                'mezcla de Google, Facebook y Twitter. Tengo un presupuesto de 200€. ¿Será suficiente?'.capitalize(),
                    category='OTHER',
                    created_by='Anna',
                ),
            ]
            self.issues.extend(more_issues)


    def add_issue(self, issue):
        self.issues.append(issue)

    def get_issues(self):
        return self.issues

    def sort_issues_by_option(self, category):
        if category == 'id':
            return sorted(self.issues, key=lambda x: x.bug_id)
        if category == 'title':
            return sorted(self.issues, key=lambda x: x.title)
        if category == 'description':
            return sorted(self.issues, key=lambda x: x.description)
        if category == 'category':
            return sorted(self.issues, key=lambda x: x.category)
        if category == 'status':
            return sorted(self.issues, key=lambda x: x.status)
        if category == 'date':
            return sorted(self.issues, key=lambda x: x.date)
        if category == 'created_by':
            return sorted(self.issues, key=lambda x: x.created_by)
        raise ValueError(f'Invalid category: {category} in Storage.sort_issues_by_option()')

    def filter_issues_by_option(self, category, value):
        if category == 'id':
            return sorted([i for i in self.issues if str(value).lower() in str(i.bug_id).lower()], key=lambda x: x.bug_id)
        if category == 'title':
            return sorted([i for i in self.issues if value.lower() in i.title.lower()], key=lambda x: x.title)
        if category == 'description':
            return sorted([i for i in self.issues if value.lower() in i.description.lower()], key=lambda x: x.description)
        if category == 'category':
            return sorted([i for i in self.issues if value.lower() in i.category.lower()], key=lambda x: x.category)
        if category == 'status':
            return sorted([i for i in self.issues if str(value).lower() == str(i.status.value).lower()], key=lambda x: x.status)
        if category == 'created_by':
            return sorted([i for i in self.issues if value.lower() in i.created_by.lower()], key=lambda x: x.created_by)
        if category == 'participant':
            return sorted([i for i in self.issues if value.lower() in [p.lower() for p in i.participants()]], key=lambda x: x.created_by)

        raise ValueError(f'Invalid category: {category} in Storage.filter_issues_by_option()')
