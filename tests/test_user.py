#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User
from models import storage
from console import HBNBCommand
from io import StringIO
import sys
import os

class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_instantiation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_before_updated_at(self):
        user1 = User()
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_str_representation(self):
        user = User()
        user.id = "12345678"
        dt = datetime.today()
        user.created_at = user.updated_at = dt
        user_str = str(user)
        self.assertIn("[User] (12345678)", user_str)
        self.assertIn("'id': '12345678'", user_str)
        self.assertIn("'created_at': " + repr(dt), user_str)
        self.assertIn("'updated_at': " + repr(dt), user_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        user = User(id="123", created_at=dt, updated_at=dt)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUpClass(cls):
        cls.backup_file = "file.json"
        cls.temp_file = "tmp"

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename(cls.temp_file, cls.backup_file)
        except FileNotFoundError:
            pass

    def setUp(self):
        os.rename(self.backup_file, self.temp_file)

    def tearDown(self):
        os.remove(self.backup_file)
        os.rename(self.temp_file, self.backup_file)

    def test_save_method(self):
        user = User()
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_save_updates_file(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as file:
            self.assertIn(user_id, file.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Alberton"
        user.my_number = 99
        user_dict = user.to_dict()
        self.assertEqual("Alberton", user.middle_name)
        self.assertIn("my_number", user_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
