#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import models
import unittest
import os
from datetime import datetime
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class."""

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
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIn(amenity, storage.all().values())
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(Amenity.name, str)

    def test_created_at_before_updated_at(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amenity = Amenity()
        amenity.id = "12345678"
        amenity.created_at = amenity.updated_at = dt
        expected_str = f"[Amenity] (12345678) {amenity.to_dict()}"
        self.assertEqual(str(amenity), expected_str)

    def test_save_method(self):
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenity_id = f"Amenity.{amenity.id}"
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())

    def test_to_dict_method(self):
        amenity = Amenity()
        amenity.middle_name = "Alberton"
        amenity.my_number = 99
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)
        self.assertIn("middle_name", amenity_dict)
        self.assertIn("my_number", amenity_dict)

if __name__ == "__main__":
    unittest.main()
