#!/usr/bin/python3
"""a module of a class"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file \
    and deserializes JSON file to instances"""

    def __init__(self):
        """initializes the class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dict"""
        return self.__objects

    def new(self, obj):
        """sets the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serialises self"""
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes instances got from json file"""
        try:
            with open(self.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                from models.base_model import BaseModel
                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        self.__objects[key] = User(**value)
                    elif value['__class__'] == 'State':
                        self.__objects[key] = State(**value)
                    elif value['__class__'] == 'City':
                        self.__objects[key] = City(**value)
                    elif value['__class__'] == 'Amenity':
                        self.__objects[key] = Amenity(**value)
                    elif value['__class__'] == 'Place':
                        self.__objects[key] = Place(**value)
                    elif value['__class__'] == 'Review':
                        self.__objects[key] = Review(**value)

        except FileNotFoundError:
            pass
