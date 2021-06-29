#!/usr/bin/python3
"""Defines test for amenity.py"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))

    def test_name(self):
        """Test if Amenity has attribute name and it's as an empty string"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")

    def test_creates_dict(self):
        """Test if to_dict method creates a dic with proper attrs"""
        a = Amenity()
        dic = a.to_dict()
        self.assertEqual(type(dic), dict)
        for att in a.__dict__:
            self.assertTrue(att in dic)
            self.assertTrue("__class__" in dic)

    def test_Not_None(self):
        """check docstrings for existing functions"""
        a = Amenity()
        self.assertIsNotNone(a.__doc__)

    def test_before_save(self):
        """check the created_at and update_a using the save method"""
        a = Amenity()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_save(self):
        """check the created_at and update_a using the save method"""
        a = Amenity()
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        a = Amenity()
        a.name = "Pool"
        self.assertTrue('id' in a.__dict__)
        self.assertTrue('created_at' in a.__dict__)
        self.assertTrue('updated_at' in a.__dict__)
        self.assertTrue('name' in a.__dict__)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        a = Amenity()
        dic = a.to_dict()
        self.assertEqual(dic["__class__"], "Amenity")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], a.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        a = Amenity()
        string = "[Amenity] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(string, str(a))


if __name__ == "__main__":
    unittest.main()
