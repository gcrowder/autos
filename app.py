from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.backends import sqlalchemy_backend
from db import settings


def welcome(name=None):
    """ Welcome to API Star. Personalized for name """
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def square(num: int = 0):
    """ Square any number """
    return {
        'message': num**2
    }


routes = [
    Route('/', 'GET', welcome),
    Route('/square/{num}', 'GET', square),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(
    routes=routes,
    settings=settings,
    commands=sqlalchemy_backend.commands,  # Install custom commands.
    components=sqlalchemy_backend.components  # Install custom components.
)


if __name__ == '__main__':
    app.main()
