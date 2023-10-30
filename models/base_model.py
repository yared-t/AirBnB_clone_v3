#!/usr/bin/python3
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """class used to define the base model
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """intialazation of the base claass
        Args:
            args: used to store the arduments
            kwargs: argumaents for the constructor
        Attributes:
            id: stores the unique id
            created_at: used to know the created 
            updated_at: used to know the updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            # TODO: wtf? more error checking?
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """used tos tore the string
        Return:
            returns the string
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.to_dict())

    def __repr__(self):
        """represantation of the string
        """
        return self.__str__()

    def save(self):
        """used to update the new ones
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """used to create the dictionery
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """used to delete the strings"""
        models.storage.delete(self)
