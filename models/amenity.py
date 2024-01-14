#!/usr/bin/python3
"""Defines the Amenity class."""
from pydantic import BaseModel
from typing import List
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity model with name attribute.

    Attributes:
    - name: str - empty string
    """
    name: str = ''
