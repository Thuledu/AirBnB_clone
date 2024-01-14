#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State model with name attribute.

    Attributes:
    - name: str - empty string
    """
    name: str = ''
