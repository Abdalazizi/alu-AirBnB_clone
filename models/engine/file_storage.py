#!/usr/bin/python3
"""
Defines the FileStorage class, which serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from typing import Any, Dict, Type

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (Dict[str, Any]): A dictionary of instantiated objects.
    """
    __file_path: str = "file.json"
    __objects: Dict[str, Any] = {}

    def all(self) -> Dict[str, Any]:
        """
        Returns the dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj: Any) -> None:
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (Any): The object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self) -> None:
        """
        Serializes the storage dictionary to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self) -> None:
        """
        Deserializes the JSON file to the storage dictionary, if the file
        exists.
        """
        try:
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                # A mapping of class names to class objects for secure
                # and efficient deserialization.
                class_map: Dict[str, Type[BaseModel]] = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Place": Place,
                    "Amenity": Amenity,
                    "Review": Review,
                }
                for obj_data in obj_dict.values():
                    class_name = obj_data.pop("__class__", None)
                    if class_name and class_name in class_map:
                        cls = class_map[class_name]
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass
