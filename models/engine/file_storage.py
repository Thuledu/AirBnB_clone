#!/usr/bin/python3
"""Defines the FileStorage class.""" 
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for serializing and deserializing instances to JSON file and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            new_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    cls_name = v["__class__"]
                    if cls_name == "User":
                        obj = User(**v)
                    elif cls_name == "State":
                        obj = State(**v)
                    elif cls_name == "City":
                        obj = City(**v)
                    elif cls_name == "Amenity":
                        obj = Amenity(**v)
                    elif cls_name == "Place":
                        obj = Place(**v)
                    elif cls_name == "Review":
                        obj = Review(**v)
                    else:
                        obj = BaseModel(**v)
                    self.__objects
                    self.__objects[k] = obj
        except FileNotFoundError:
            return
