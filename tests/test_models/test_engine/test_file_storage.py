#!/usr/bin/python3
"""Module Test Case for FileStorage"""
import unittest
from datetime import datetime
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import json
import models
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """" Test cases class for FileStorage """
    @classmethod
    def setUpClass(cls):
        cls.p1 = Place()
        cls.p1.city_id = "Richmond"
        cls.p1.state_id = "VA"
        cls.p1.number_rooms = 8
        cls.p1.description = "awesome"

    @classmethod
    def tearDownClass(cls):
        del cls.p1

    def setUp(self):
        """ Setup function for TestFileStorage """
        super().setUp()
        self.file_path = 'file.json'

    def test_instance_creation(self):
        """ Test for FfileStorage instance creation """
        my_storage = FileStorage()
        self.assertIs(type(my_storage), FileStorage)

    def test_all_returns_dict(self):
        """testing the types"""
        storage_dict = storage.all()
        self.assertEqual(type(storage_dict), dict)
        self.assertIs(storage_dict, storage._FileStorage__objects)

    def test_method_all_with_one_param(self):
        """ Tests for method 'all' with one param """

        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all([])
        with self.assertRaisesRegex(TypeError, regex):
            storage.all([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.all(dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.all({'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.all('Ranmod value')

    def test_method_new(self):
        """ Test that 'new' method stores an object correctly """
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        all_objs = storage.all()
        storage.new(obj)

        self.assertEqual(obj, all_objs[key])

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_method_new_with_one_param(self):
        """ Tests for method 'new' with one param different than expected """

        regex = "object has no attribute 'id'"
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(None)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new([])
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new([1, 2, 3])
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({1, 2, 3})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(True)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(False)
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new(dict())
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new({'id': 123})
        with self.assertRaisesRegex(AttributeError, regex):
            storage.new('Ranmod value')

    def test_method_new_with_two_params(self):
        """ Test 'new' method with two positional args """
        obj = BaseModel()

        regex = 'takes 2 positional arguments but 3 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, [])
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, {'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.new(obj, 'Ranmod value')

    def test_save_method(self):
        """ Tests for 'save' method """
        prev_all_objs = storage.all()

        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)

        self.assertIn(key, prev_all_objs.keys())
        try:

            with open('file.json', mode='r', encoding='utf-8') as file:
                dict_loaded = json.load(file)

                self.assertIs(type(dict_loaded), dict)
                self.assertNotIn(key, dict_loaded.keys())

            storage.save()
        except FileNotFoundError:
            pass
        try:

            with open('file.json', mode='r', encoding='utf-8') as file:
                dict_loaded = json.load(file)

                self.assertIs(type(dict_loaded), dict)
                self.assertIn(key, dict_loaded.keys())
        except FileNotFoundError:
            pass

    def test_save_method_with_one_param(self):
        """ Test for 'save' method with one param """
        regex = 'takes 1 positional argument but 2 were given'
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(None)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save([])
        with self.assertRaisesRegex(TypeError, regex):
            storage.save([1, 2, 3])
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({1, 2, 3})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(True)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(False)
        with self.assertRaisesRegex(TypeError, regex):
            storage.save(dict())
        with self.assertRaisesRegex(TypeError, regex):
            storage.save({'id': 123})
        with self.assertRaisesRegex(TypeError, regex):
            storage.save('Ranmod value')

    def test_reload_method(self):
        """ Test cases for 'reload' method """
        prev_dict = storage.all()

        storage.reload()

        self.assertDictEqual(prev_dict, storage.all())

    def test_reload_method_with_one_param(self):
        """ Tests for reload method passing one param """
        with self.assertRaises(TypeError):
            storage.reload(None)
        with self.assertRaises(TypeError):
            storage.reload([])
        with self.assertRaises(TypeError):
            storage.reload([1, 2, 3])
        with self.assertRaises(TypeError):
            storage.reload({})
        with self.assertRaises(TypeError):
            storage.reload({1, 2, 3})
        with self.assertRaises(TypeError):
            storage.reload(True)
        with self.assertRaises(TypeError):
            storage.reload(False)
        with self.assertRaises(TypeError):
            storage.reload(dict())
        with self.assertRaises(TypeError):
            storage.reload({'id': 123})
        with self.assertRaises(TypeError):
            storage.reload('Ranmod value')

    def test_errs(self):
        """Test most mal usage of FileStorage methods"""
        b1 = BaseModel()
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_path

        with self.assertRaises(TypeError):
            models.storage.new()
            models.storage.new(self, b1)
            models.save(b1)
            models.reload(b1)
            models.all(b1)

    def test_fs_instance(self):
        """FileStorage class save checks, reload checks"""
        b1 = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_pep8_base_model(self):
        """
        pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_instance_creation(self):
        """ Test for FfileStorage instance creation """
        my_storage = FileStorage()
        self.assertIs(type(my_storage), FileStorage)

    def test_method_all(self):
        """ Test method 'all' of storage """
        all = storage.all()
        empty_dict = dict()

        if os.path.exists(self.file_path):
            self.assertNotEqual(all, empty_dict)
        else:
            self.assertDictEqual(all, empty_dict)

if __name__ == '__main__':
    unittest.main()
