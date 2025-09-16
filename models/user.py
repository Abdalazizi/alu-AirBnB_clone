#!/usr/bin/python3
"""
Defines the User class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User in the HBnB project.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
