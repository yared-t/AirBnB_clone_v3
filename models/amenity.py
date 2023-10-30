#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """class used to amenity
    Attributes:
        name: name input
    """
    __tablename__ = "amenities"
    name = Column(String(128),
                  nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            viewonly=False,
            back_populates="amenities")
