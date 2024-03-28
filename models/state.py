#!/usr/bin/python3
from sqlalchemy import Column
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    cities = relationship('City', cascade='all, delete-orphan', backref='state')
