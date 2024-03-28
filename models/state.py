#!/usr/bin/python3
from sqlalchemy import Column
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    cities = relationship('City', cascade='all, delete-orphan', backref='state')
    
    @property
    def cities(self):
        """Getter attribute to return list of City instances with matching state_id"""
        from models import storage
        
        all_cities = storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
