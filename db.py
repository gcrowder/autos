from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Enum
from sqlalchemy.orm import relationship
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.backends import sqlalchemy_backend

Base = declarative_base()

class Auto(Base):
    """ Auto describes automobiles """
    __tablename__ = "Auto"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(String(4))
    fuel_stops = relationship("FuelStop", back_populates="auto")

    def __repr__(self):
        return f'{self.year} {self.make} {self.model}'

    def __string__(self):
        return f'{self.year} {self.make} {self.model}'


class FuelStop(Base):
    __tablename__ = "FuelStop"
    id = Column(Integer, primary_key=True)

    auto_id = Column(Integer, ForeignKey('auto.id'))
    auto = relationship("Auto", back_populates="fuel_stops")
    odometer = Column(Integer)
    time_of_stop = Column(TIMESTAMP)
    octane = Column(Enum("85", "87", "89", "91", "93"))
    

class FuelStation(Base):
    __tablename__ = "FuelStation"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

routes = [
    # ...
]

# Configure database settings.
settings = {
    "DATABASE": {
        "URL": "sqlite:///autos.db",
        "METADATA": Base.metadata
    }
}

"""
app = App(
    routes=routes,
    settings=settings,
    commands=sqlalchemy_backend.commands,  # Install custom commands.
    components=sqlalchemy_backend.components  # Install custom components.
)
"""