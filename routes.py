from apistar import http, Route
from apistar.backends.sqlalchemy_backend import Session
from db import Auto


def make_auto_dict(auto: Auto) -> dict:
    return {
        "id": auto.id,
        "name": auto.name,
        "make": auto.make,
        "model": auto.model,
        "year": auto.year
    }

def create_auto(session: Session, data: http.RequestData) -> dict:
    """ Creates auto in db. Called from POST /autos/ """
    auto = Auto(**data)
    session.add(auto)
    session.flush()
    return make_auto_dict(auto)

def list_autos(session: Session) -> list:
    """ Lists autos from db. Called from GET /autos/ """
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

def get_auto(session: Session, auto_id: int) -> dict:
    """ Get an auto from db by id. Called from GET /autos/:id """
    auto = session.query(Auto).get(auto_id)
    return make_auto_dict(auto)

def update_auto(session: Session, auto_id: int, data: http.RequestData) -> dict:
    """ Update a given auto. Called from PATCH /autos/:id """
    auto_properties = ["name", "make", "model", "year"]
    auto = session.query(Auto).get(auto_id)
    for auto_prop in auto_properties:
        if auto_prop in data:
            setattr(auto, auto_prop, data[auto_prop])
    session.flush()
    return make_auto_dict(auto)

def delete_auto(session: Session, auto_id: int, data: http.RequestData) -> None:
    """ Delete a given auto. Called from DELETE /autos/:id """
    auto = session.query(Auto).get(auto_id)
    session.delete(auto)
    session.flush()
    return None

auto_urls = [
    Route('/', 'GET', list_autos),
    Route('/', 'POST', create_auto),
    Route('/{auto_id}', 'PATCH', update_auto),
    Route('/{auto_id}', 'DELETE', delete_auto),
    Route('/{auto_id}', 'GET', get_auto)
]