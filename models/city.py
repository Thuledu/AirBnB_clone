#!/usr/bin/python3
"""Defines the City class."""
from pydantic import BaseModel
from models.base_model import BaseModel

class City(BaseModel):
    """
    City model with state_id and name attributes.

    Attributes:
    - state_id: str - empty string: it will be the State.id
    - name: str - empty string
    """
    state_id: str = ''
    name: str = ''
