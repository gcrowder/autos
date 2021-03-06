from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.backends import sqlalchemy_backend
from db import settings
from routes import auto_urls


def welcome(name=None):
    """ Welcome to API Star. Personalized for name """
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', 'GET', welcome),
    Include('/autos', auto_urls),
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
