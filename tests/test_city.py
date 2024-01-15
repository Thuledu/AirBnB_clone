#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
import os
from datetime import datetime
from models.city import City
from models import storage

class TestCity(unittest.TestCase):
    """Unittests for the City class."""

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
        city = City()
        self.assertIsInstance(city, City)
        self.assertIn(city, storage.all().values())
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

    def test_created_at_before_updated_at(self):
        city1 = City()
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

     def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        city = City(id="123", created_at=dt, updated_at=dt)
        self.assertEqual(city.id, "123")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        city = City()
        city.id = "12345678"
        city.created_at = city.updated_at = dt
        expected_str = f"[City] (12345678) {city.to_dict()}"
        self.assertEqual(str(city), expected_str)

    def test_save_method(self):
        city = City()
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_save_updates_file(self):
        city = City()
        city.save()
        city_id = f"City.{city.id}"
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())

    def test_to_dict_method(self):
        city = City()
        city.middle_name = "Alberton"
        city.my_number = 99
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("middle_name", city_dict)
        self.assertIn("my_number", city_dict)
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))
        self.assertEqual("Alberton", city_dict["middle_name"])
        self.assertEqual(99, city_dict["my_number"])

if __name__ == "__main__":
    unittest.main()
