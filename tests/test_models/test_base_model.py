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

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_init(self):
        """check if an instance was created upon initialization"""
        self.assertTrue(isinstance(self.b, BaseModel))

    def test_kwargs(self):
        """Kwargs input on BaseModel instantiation"""
        b_dict = self.b.to_dict()
        b2 = BaseModel(**b_dict)
        b2_dict = b2.to_dict()
        self.assertEqual(
            b2_dict['updated_at'].split('T')[0], str(
                self.b.updated_at).split()[0])
        self.assertEqual(
            b2_dict['created_at'].split('T')[1], str(
                self.b.created_at).split()[1])
        self.assertEqual(b2_dict['id'], self.b.id)
        self.assertEqual(b2_dict['__class__'], type(self.b).__name__)

    def test_save(self):
        """check save function of BaseModel"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

if __name__ == '__main__':
    unittest.main()
