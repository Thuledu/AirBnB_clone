#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_init(self):
        """
        Test the initialization of the BaseModel class.
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_instance_creation(self):
        """
        Test the instance creation of the BaseModel class.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string method of the BaseModel
        """
        self.assertEqual(str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}")

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.model.updated_at.isoformat())

    def test_reload_method(self):
        # Save the model to file
        storage.save()
        # Create a new model instance
        new_model = BaseModel()
        # Reload the data from file
        storage.reload()
        # Check if the new model is in the storage
        self.assertIn(new_model.id, storage.all().keys())

if __name__ == '__main__':
    unittest.main()
