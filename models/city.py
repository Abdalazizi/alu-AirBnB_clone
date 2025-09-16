#!/usr/bin/python3
"""
Defines the City class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City in the HBnB project.

    Attributes:
        state_id (str): The ID of the state this city belongs to.
        name (str): The name of the city.
    """

    state_id: str = ""
    name: str = ""
