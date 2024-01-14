#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User
from models import storage
from console import HBNBCommand
from io import StringIO
import sys


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_user_attributes(self):
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_save(self):
        new_user = User()
        new_user.save()
        all_users = storage.all()
        key = "User." + new_user.id
        self.assertIn(key, all_users)

    def test_user_destroy(self):
        new_user = User()
        new_user.save()
        all_users = storage.all()
        key = "User." + new_user.id
        self.assertIn(key, all_users)
        destroy_cmd = "destroy User " + new_user.id
        HBNBCommand().onecmd(destroy_cmd)
        all_users = storage.all()
        self.assertNotIn(key, all_users)

    def test_user_commands_interactive_mode(self):
        commands = ["create User", "all", "show User", "update User 1234-1234-1234 email 'test@test.com'"]
        for cmd in commands:
            HBNBCommand().onecmd(cmd)

    def test_user_commands_non_interactive_mode(self):
        commands = ["create User\n", "all\n", "show User\n", "update User 1234-1234-1234 email 'test@test.com'\n"]
        for cmd in commands:
            sys.stdin = StringIO(cmd)
            HBNBCommand().cmdloop()

if __name__ == '__main__':
    unittest.main()
