from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Enum
from sqlalchemy.orm import relationship



Base = declarative_base()

class Auto(Base):
    """ Auto describes automobiles """
    __tablename__ = "auto"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(String(4))
    fuel_stops = relationship("FuelStop",
                              back_populates="auto",
                              cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f'{self.year} {self.make} {self.model}'

    def __string__(self):
        return f'{self.year} {self.make} {self.model}'


class FuelStop(Base):
    """ FuelStop describes the event of getting gasoline """
    __tablename__ = "fuelstop"
    id = Column(Integer, primary_key=True)
    fuel_station_id = Column(Integer, ForeignKey('fuelstation.id'))
    fuel_station = relationship("FuelStation", back_populates="fuel_stops")
    auto_id = Column(Integer, ForeignKey('auto.id'))
    auto = relationship("Auto", back_populates="fuel_stops")
    odometer = Column(Integer)
    time_of_stop = Column(TIMESTAMP)
    octane = Column(Enum("85", "87", "89", "91", "93"))


class FuelStation(Base):
    """ FuelStation describes a gas station """
    __tablename__ = "fuelstation"
    id = Column(Integer, primary_key=True)
    fuel_stops = relationship("FuelStop", back_populates="fuel_station")
    name = Column(String)
    latitude = Column(String)
    longitute = Column(String)


# Configure database settings.
settings = {
    "DATABASE": {
        "URL": "sqlite:///autos.db",
        "METADATA": Base.metadata
    }
}