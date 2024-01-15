#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import unittest
import os
from datetime import datetime
from models.review import Review
from models import storage

class TestReview(unittest.TestCase):
    """Unittests for the Review class."""

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
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIn(review, storage.all().values())
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

     def test_created_at_before_updated_at(self):
        review1 = Review()
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)
        self.assertLess(review1.updated_at, review2.updated_at)

     def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "123")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        review = Review()
        review.id = "12345678"
        review.created_at = review.updated_at = dt
        expected_str = f"[Review] (12345678) {review.to_dict()}"
        self.assertEqual(str(review), expected_str)

     def test_save_method(self):
        review = Review()
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_save_updates_file(self):
        review = Review()
        review.save()
        review_id = f"Review.{review.id}"
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())

    def test_to_dict_method(self):
        review = Review()
        review.middle_name = "Alberton"
        review.my_number = 99
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("middle_name", review_dict)
        self.assertIn("my_number", review_dict)

if __name__ == "__main__":
    unittest.main()
