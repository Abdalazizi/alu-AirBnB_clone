#!/usr/bin/python3
"""
Defines the BaseModel class, the foundation for all other models in the HBnB
project.
"""
import models
from uuid import uuid4
from datetime import datetime
from typing import Any, Dict


class BaseModel:
    """
    Represents the BaseModel of the HBnB project.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last
                               updated.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes a new BaseModel instance.

        Args:
            *args (Any): Not used.
            **kwargs (Any): A dictionary of attribute key-value pairs.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(str(value), tform))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self) -> None:
        """
        Updates the `updated_at` attribute with the current datetime and saves
        the instance to the storage.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the BaseModel instance.

        This dictionary includes a `__class__` key with the class name of the
        object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self) -> str:
        """
        Returns the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
