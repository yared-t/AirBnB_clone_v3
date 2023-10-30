#!/usr/bin/python3
"""it is used to json files"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """used to serializes instances
    Attributes:
        __file_path: used to know the oath of json
        __objects: used to store the objects
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None)
    """used to delete
        Args:
            obj: used to store the object
        """
        if not obj:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def all(self, cls=None):
        """used to return all
        Args:
            cls: used to class the dictionery
        """
        if not cls:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if type(v) == cls}

    def new(self, obj):
        """used to set the new objects
        Args:
            obj: used to storet he object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """path to json
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """used to note the path of json
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """used to restore the json"""
        self.reload()
