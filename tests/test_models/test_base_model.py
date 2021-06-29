#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime
import unittest
import pep8

class TestBaseModel(unittest.TestCase):
    """
    Test cases class
    """
    @classmethod
    def setUpClass(cls):
        cls.b = BaseModel()

    def test_check_pep8(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Solving pep8")

    def test_base_instance(self):
        """b is an instance of BaseModel"""
        self.assertIsInstance(self.b, BaseModel)

    def test_attributes(self):
        """Tests Public Attributes of BaseModel instances"""
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)
        self.assertEqual(str(self.b.created_at).split('.')[0],
                         str(self.b.updated_at).split('.')[0])

    def test_Not_None(self):
        """check existence of docstring in BaseModel functions"""
        b = BaseModel()
        self.assertIsNotNone(b.__doc__)
        self.assertIsNotNone(b.save.__doc__)
        self.assertIsNotNone(b.to_dict.__doc__)

    def test_more_attributes(self):
        """check if attributes exists"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "__init__"))
        self.assertTrue(hasattr(b, "save"))
        self.assertTrue(hasattr(b, "to_dict"))

if __name__ == '__main__':
    unittest.main()
