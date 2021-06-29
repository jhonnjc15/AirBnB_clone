#!/usr/bin/python3
"""Defines unittests for place.py"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Tests for Place Class"""
    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id(self):
        """Test if Place has attr city_id and it's empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

if __name__ == "__main__":
    unittest.main()
