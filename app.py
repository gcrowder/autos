from apistar import Include, Route, http
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.backends import sqlalchemy_backend
from apistar.backends.sqlalchemy_backend import Session
from db import settings, Auto

def make_auto_dict(auto: Auto) -> dict:
    return {
        "id": auto.id,
        "name": auto.name,
        "make": auto.make,
        "model": auto.model,
        "year": auto.year
    }



def create_auto(session: Session, data: http.RequestData):
    """ Creates auto in db. Called from POST /autos """
    auto = Auto(**data)
    session.add(auto)
    session.flush()
    return make_auto_dict(auto)

def list_autos(session: Session):
    """ Lists autos from db. Called from GET /autos """
    queryset = session.query(Auto).all()
    return [
        {
            "id": auto.id,
            "name": auto.name,
            "make": auto.make,
            "model": auto.model,
            "year": auto.year
        }
        for auto in queryset
    ]

def get_auto(session: Session, auto_id: int):
    """ Get an auto from db by id. Called from GET /autos/:id """
    auto = session.query(Auto).get(auto_id)
    return make_auto_dict(auto)

def update_auto(session: Session, auto_id: int, data: http.RequestData):
    """ Update a given auto. Called from PATCH /autos/:id """
    auto_properties = ["name", "make", "model", "year"]
    auto = session.query(Auto).get(auto_id)
    for auto_prop in auto_properties:
        if auto_prop in data:
            setattr(auto, auto_prop, data[auto_prop])
    session.flush()
    return make_auto_dict(auto)

def delete_auto(session: Session, auto_id: int, data: http.RequestData):
    """ Delete a given auto. Called from DELETE /autos/:id """
    auto = session.query(Auto).get(auto_id)
    session.delete(auto)
    session.flush()
    return None

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
    Route('/autos', 'POST', create_auto),
    Route('/autos', 'GET', list_autos),
    Route('/autos/{auto_id}', 'GET', get_auto),
    Route('/autos/{auto_id}', 'PATCH', update_auto),
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
