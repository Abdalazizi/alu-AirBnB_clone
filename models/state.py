#!/usr/bin/python3
"""
Defines the State class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a State in the HBnB project.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""
