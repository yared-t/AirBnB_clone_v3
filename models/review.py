#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """class for the review
    Attributes:
        place_id: used to store the palce id
        user_id: used to storet he user id
        text: used to review the description
    """
    __tablename__ = "reviews"
    text = Column(String(1024),
                  nullable=False)
    place_id = Column(String(60),
                      ForeignKey("places.id", ondelete="CASCADE"),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
