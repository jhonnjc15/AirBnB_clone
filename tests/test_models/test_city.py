#!/usr/bin/python3
"""Define tests for city.py"""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        c = City()
        self.assertIsInstance(c, BaseModel)
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))

    def test_name(self):
        """Test if City has attribute name and it's an empty string"""
        c = City()
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.name, "")

    def test_state_id(self):
        """Test if City has attribute state_id and it's an empty string"""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertEqual(c.state_id, "")

    def test_creates_dict(self):
        """Test if to_dict method creates a dictionary with proper attrs"""
        c = City()
        dic = c.to_dict()
        self.assertEqual(type(dic), dict)
        for att in c.__dict__:
            self.assertTrue(att in dic)
            self.assertTrue("__class__" in dic)

    def test_dict_values(self):
        """Test if values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        dic = c.to_dict()
        self.assertEqual(dic["__class__"], "City")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """Test str method"""
        c = City()
        string = "[City] ({}) {}".format(c.id, c.__dict__)
        self.assertEqual(string, str(c))
