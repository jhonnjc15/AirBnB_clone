#!/usr/bin/python3
"""Define tests for user.py"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_email(self):
        """Test if User has attr email and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")

    def test_password(self):
        """Test if User has attr password and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")

    def test_first_name(self):
        """Test if User has attr first_name and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")

    def test_last_name(self):
        """Test if User has attr last_name and it's an empty string"""
        u = User()
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")

    def test_creates_dict(self):
        """Test if to_dict method creates a dic with proper attrs"""
        u = User()
        dic = u.to_dict()
        self.assertEqual(type(dic), dict)
        for att in u.__dict__:
            self.assertTrue(att in dic)
            self.assertTrue("__class__" in dic)

    def test_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        dic = u.to_dict()
        self.assertEqual(dic["__class__"], "User")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        u = User()
        string = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(string, str(u))


if __name__ == "__main__":
    unittest.main()
