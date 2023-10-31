#!/usr/bin/python3
#Author: MikiasHailu and YaredTsgine
""" This module will Contain the FileStorage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """ This class will serializes instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """This function will return the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """ This function will sets in __object"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ This fucntion will serializes __objects to the JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ This fucntion will deserializes the JSON file """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """ This fucntion will delete obj """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """ This fucntionw will call the method reload for deserializing the JSON file to objects """
        self.reload()

    def get(self, cls, id):
        """ This fucntion is a get request """
        if cls and id:
            takeObj = '{}.{}'.format(cls, id)
            everyObj = self.all(cls)
            return everyObj.get(takeObj)
        else:
            return None

    def count(self, cls=None):
        """ This fucntion is the count fucntion """
        return (len(self.all(cls)))
