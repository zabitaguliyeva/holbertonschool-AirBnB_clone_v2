#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


association_table = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    amenities = relationship("Amenity",
                             secondary="place_amenity",
                             viewonly=False)
    reviews = relationship("Review", backref="place",
                           cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            arr = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    arr.append(amenity)
            return arr

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)

        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            arr = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    arr.append(review)
            return arr
