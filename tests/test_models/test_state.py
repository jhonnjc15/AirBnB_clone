#!/usr/bin/python3
"""Defines test for state.py"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel"""
        s = State()
        self.assertIsInstance(s, BaseModel)
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))

    def test_name(self):
        """Test if State has attribute name and it's as an empty string"""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

    def test_creates_dict(self):
        """Test if to_dict method creates a dic with proper attrs"""
        s = State()
        dic = s.to_dict()
        self.assertEqual(type(dic), dict)
        for att in s.__dict__:
            self.assertTrue(att in dic)
            self.assertTrue("__class__" in dic)

    def test_Not_None(self):
        """check docstrings for existing functions"""
        s = State()
        self.assertIsNotNone(s.__doc__)

    def test_before_save(self):
        """check the created_at and update_a using the save method"""
        s = State()
        self.assertNotEqual(s.created_at, s.updated_at)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        s = State()
        self.assertTrue('id' in s.__dict__)
        self.assertTrue('created_at' in s.__dict__)
        self.assertTrue('updated_at' in s.__dict__)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        dic = s.to_dict()
        self.assertEqual(dic["__class__"], "State")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        s = State()
        string = "[State] ({}) {}".format(s.id, s.__dict__)
        self.assertEqual(string, str(s))


if __name__ == "__main__":
    unittest.main()
