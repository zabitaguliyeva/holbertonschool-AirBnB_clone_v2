#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states_id'), nullable = False)
    name = Column(String(128), nullable = false)
