#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import unittest
import os
from datetime import datetime
from models.place import Place
from models import storage

class TestPlace(unittest.TestCase):
    """Unittests for the Place class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIn(place, storage.all().values())
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)

     def test_created_at_before_updated_at(self):
        place1 = Place()
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        place = Place(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(place.id, "123")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        place = Place()
        place.id = "12345678"
        place.created_at = place.updated_at = dt
        expected_str = f"[Place] (12345678) {place.to_dict()}"
        self.assertEqual(str(place), expected_str)

    def test_save_method(self):
        place = Place()
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_save_updates_file(self):
        place = Place()
        place.save()
        place_id = f"Place.{place.id}"
        with open("file.json", "r") as f:
            self.assertIn(place_id, f.read())

    def test_to_dict_method(self):
        place = Place()
        place.middle_name = "Alberton"
        place.my_number = 99
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)
        self.assertIn("middle_name", place_dict)
        self.assertIn("my_number", place_dict)

if __name__ == "__main__":
    unittest.main()
