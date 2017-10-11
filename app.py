from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls


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

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
