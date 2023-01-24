#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.city import City
from models.review import Review
from models.amenity import Amenity

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="places",
                                 viewonly=False)

    if models.storage_type != 'db':
        @property
        def reviews(self):
            """
            getter for the review attributes
            """
            my_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    my_list.append(review)
            return my_list

        @property
        def amenities(self):
            """
            getter for the amenity attributes
            """
            my_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    my_list.append(amenity)
            return my_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter method for amenities
            """
            if (type(obj) == Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
