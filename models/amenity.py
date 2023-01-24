#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')

    def __init__(self, *args, **kwargs):
        """
        initi amenity
        """
        super().__init__(*args, **kwargs)
