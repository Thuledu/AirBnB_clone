#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
import os
from datetime import datetime
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """Unittests for the State class."""

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
        state = State()
        self.assertIsInstance(state, State)
        self.assertIn(state, storage.all().values())
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(State.name, str)

     def test_created_at_before_updated_at(self):
        state1 = State()
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

     def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state = State()
        state.id = "12345678"
        state.created_at = state.updated_at = dt
        expected_str = f"[State] (12345678) {state.to_dict()}"
        self.assertEqual(str(state), expected_str)

     def test_save_method(self):
        state = State()
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_save_updates_file(self):
        state = State()
        state.save()
        state_id = f"State.{state.id}"
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())

    def test_to_dict_method(self):
        state = State()
        state.middle_name = "Alberton"
        state.my_number = 99
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertIn("middle_name", state_dict)
        self.assertIn("my_number", state_dict)

if __name__ == "__main__":
    unittest.main()
