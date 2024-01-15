#!/usr/bin/python3
"""Defines unittests for console.py."""
import unittest
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase):
    """Unittests for testing the console functionality."""

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Prints the string representation of an instance", output)

class TestParseNonInteractive(unittest.TestCase):
    """Unittests for the parse function in non-interactive mode."""

    def test_parse_no_braces_or_brackets(self):
        input_str = "This is a test string"
        expected_output = ["This", "is", "a", "test", "string"]
        self.assertEqual(parse(input_str), expected_output)

    def test_parse_with_curly_braces(self):
        input_str = "This is a {test} string"
        expected_output = ["This", "is", "a", "{test}", "string"]
        self.assertEqual(parse(input_str), expected_output)

    def test_parse_with_square_brackets(self):
        input_str = "This is a [test] string"
        expected_output = ["This", "is", "a", "[test]", "string"]
        self.assertEqual(parse(input_str), expected_output)

class TestParseInteractive(unittest.TestCase):
    """Unittests for the parse function in interactive mode."""

    def test_parse_no_braces_or_brackets(self):
        input_str = "This is a test string"
        expected_output = ["This", "is", "a", "test", "string"]
        self.assertEqual(parse(input_str), expected_output)

    def test_parse_with_curly_braces(self):
        input_str = "This is a {test} string"
        expected_output = ["This", "is", "a", "{test}", "string"]
        self.assertEqual(parse(input_str), expected_output)

    def test_parse_with_square_brackets(self):
        input_str = "This is a [test] string"
        expected_output = ["This", "is", "a", "[test]", "string"]
        self.assertEqual(parse(input_str), expected_output)

class TestHBNBCommandNonInteractive(unittest.TestCase):
    """Unittests for the HBNBCommand class in non-interactive mode."""

    def test_default_behavior_invalid_input(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().default("invalid_command")

    def test_do_create_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("create")

    def test_do_create_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("create NonExistentClass")

class TestHBNBCommandInteractive(unittest.TestCase):
    """Unittests for the HBNBCommand class in interactive mode."""

    def test_default_behavior_invalid_input(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().default("invalid_command")
            output = f.getvalue().strip()
            self.assertIn("invalid_command", output)

    def test_do_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_do_create_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

class TestDoShowInteractive(unittest.TestCase):
    """Unittests for the do_show method in interactive mode."""

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_show_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_show_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

class TestDoShowNonInteractive(unittest.TestCase):
    """Unittests for the do_show method in non-interactive mode."""

    def test_show_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show")

    def test_show_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show NonExistentClass")

    def test_show_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show BaseModel")

class TestDoDestroyInteractive(unittest.TestCase):
    """Unittests for the do_destroy method in interactive mode."""

    def test_destroy_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_destroy_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

class TestDoDestroyNonInteractive(unittest.TestCase):
    """Unittests for the do_destroy method in non-interactive mode."""

    def test_destroy_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy")

    def test_destroy_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy NonExistentClass")

    def test_destroy_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy BaseModel")

class TestDoAllInteractive(unittest.TestCase):
    """Unittests for the do_all method in interactive mode."""

    def test_all_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("string representations of instances", output)

class TestDoAllNonInteractive(unittest.TestCase):
    """Unittests for the do_all method in non-interactive mode."""

    def test_all_no_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("all")

class TestDoUpdateInteractive(unittest.TestCase):
    """Unittests for the do_update method in interactive mode."""

    def test_update_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_update_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_update_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_update_missing_attribute_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345")
            output = f.getvalue().strip()
            self.assertIn("** attribute name missing **", output)

    def test_update_missing_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345 name")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)

class TestDoUpdateNonInteractive(unittest.TestCase):
    """Unittests for the do_update method in non-interactive mode."""

    def test_update_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update")

    def test_update_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update NonExistentClass")

    def test_update_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel")

    def test_update_missing_attribute_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel 12345")

    def test_update_missing_value(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel 12345 name")

class TestDoCountInteractive(unittest.TestCase):
    """Unittests for the do_count method in interactive mode."""

    def test_count_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output.isdigit())

class TestDoCountNonInteractive(unittest.TestCase):
    """Unittests for the do_count method in non-interactive mode."""

    def test_count_with_class_name(self):
        result = HBNBCommand().onecmd("count BaseModel")
        self.assertTrue(result.isdigit())

class TestDoShowIdInteractive(unittest.TestCase):
    """Unittests for the do_show_id method in interactive mode."""

    def test_show_id_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_show_id_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_show_id_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

class TestDoShowIdNonInteractive(unittest.TestCase):
    """Unittests for the do_show_id method in non-interactive mode."""

    def test_show_id_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show")

    def test_show_id_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show NonExistentClass")

    def test_show_id_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("show BaseModel")

class TestDoDestroyIdInteractive(unittest.TestCase):
    """Unittests for the do_destroy_id method in interactive mode."""

    def test_destroy_id_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_destroy_id_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_id_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

class TestDoDestroyIdNonInteractive(unittest.TestCase):
    """Unittests for the do_destroy_id method in non-interactive mode."""

    def test_destroy_id_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy")

    def test_destroy_id_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy NonExistentClass")

    def test_destroy_id_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("destroy BaseModel")

class TestDoUpdateIdInteractive(unittest.TestCase):
    """Unittests for the do_update_id method in interactive mode."""

    def test_update_id_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_update_id_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_update_id_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_update_id_missing_attribute_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345")
            output = f.getvalue().strip()
            self.assertIn("** attribute name missing **", output)

    def test_update_id_missing_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345 name")
            output = f.getvalue().strip()
            self.assertIn("** value missing **", output)

class TestDoUpdateIdNonInteractive(unittest.TestCase):
    """Unittests for the do_update_id method in non-interactive mode."""

    def test_update_id_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update")

    def test_update_id_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update NonExistentClass")

    def test_update_id_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel")

    def test_update_id_missing_attribute_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel 12345")

    def test_update_id_missing_value(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel 12345 name")

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestDoUpdateDictInteractive(unittest.TestCase):
    """Unittests for the do_update_dict method in interactive mode."""

    def test_update_dict_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_update_dict_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonExistentClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_update_dict_missing_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_update_dict_missing_dictionary(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 12345")
            output = f.getvalue().strip()
            self.assertIn("** dictionary missing **", output)

class TestDoUpdateDictNonInteractive(unittest.TestCase):
    """Unittests for the do_update_dict method in non-interactive mode."""

    def test_update_dict_missing_class_name(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update")

    def test_update_dict_nonexistent_class(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update NonExistentClass")

    def test_update_dict_missing_instance_id(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel")

    def test_update_dict_missing_dictionary(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("update BaseModel 12345")

class TestConsoleMethodsInteractive(unittest.TestCase):
    """Unittests for console methods in interactive mode."""

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("EOF")
            self.assertTrue(result)

    def test_do_quit(self):
        result = HBNBCommand().onecmd("quit")
        self.assertTrue(result)

class TestConsoleMethodsNonInteractive(unittest.TestCase):
    """Unittests for console methods in non-interactive mode."""

    def test_emptyline(self):
        with self.assertRaises(AttributeError):
            HBNBCommand().onecmd("")

    def test_do_EOF(self):
        result = HBNBCommand().onecmd("EOF")
        self.assertTrue(result)

    def test_do_quit(self):
        result = HBNBCommand().onecmd("quit")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
