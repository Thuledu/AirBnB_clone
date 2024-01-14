#!/usr/bin/python3
"""Defines the Place class."""
from typing import List
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place model with specified attributes.

    Attributes:
    - city_id: str - empty string: it will be the City.id
    - user_id: str - empty string: it will be the User.id
    - name: str - empty string
    - description: str - empty string
    - number_rooms: int - 0
    - number_bathrooms: int - 0
    - max_guest: int - 0
    - price_by_night: int - 0
    - latitude: float - 0.0
    - longitude: float - 0.0
    - amenity_ids: List[str] - empty list: it will be the list of Amenity.id later
    """
    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []
