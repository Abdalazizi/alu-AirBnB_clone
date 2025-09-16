#!/usr/bin/python3
"""
Defines the Review class, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a Review in the HBnB project.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
