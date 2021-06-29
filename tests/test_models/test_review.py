#!/usr/bin/python3
"""Defines tests for review.py"""

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))

    def test_place_id(self):
        """Test if Review has attr place_id and it's an empty string"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertEqual(r.place_id, "")

    def test_user_id(self):
        """Test if Review has attr user_id and it's an empty string"""
        r = Review()
        self.assertTrue(hasattr(r, "user_id"))
        self.assertEqual(r.user_id, "")

    def test_text(self):
        """Test if Review has attr text and it's an empty string"""
        r = Review()
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.text, "")

    def test_creates_dict(self):
        """Test if to_dict method creates a dict with proper attrs"""
        r = Review()
        dic = r.to_dict()
        self.assertEqual(type(dic), dict)
        for att in r.__dict__:
            self.assertTrue(att in dic)
            self.assertTrue("__class__" in dic)

    def test_dict_values(self):
        """Test if values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        dic = r.to_dict()
        self.assertEqual(dic["__class__"], "Review")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """Test str method"""
        r = Review()
        string = "[Review] ({}) {}".format(r.id, r.__dict__)
        self.assertEqual(string, str(r))

if __name__ == "__main__":
    unittest.main()
