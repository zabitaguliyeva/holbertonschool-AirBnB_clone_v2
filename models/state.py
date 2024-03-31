#!/usr/bin/python3
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

""" State Module for HBNB project """


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute to return list of
            City instances with matching state_id"""
            from models import storage

            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
    else:
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

        @property
        def cities(self):
            """Getter attribute to return list of City
            instances with matching state_id"""
            return [city for city in self.cities]
