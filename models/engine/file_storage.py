#!/usr/bin/python3

"""file_storage.py - Create the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    FileStore class - that serializes instances to a JSON file
                        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        All Method:
            Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new Method:
            Sets in __objects the obj with key <obj class name>.id
            Args:
                obj : values
        """
        FileStorage.__objects[type(obj).__name__ + "." + str(obj.id)] = obj

    def save(self):
        """
        save Method:
            Serializes __objects to the JSON file
        """
        new_dict = {}
        for keys, values in FileStorage.__objects.items():
            new_dict[keys] = values.to_dict()
        with open(FileStorage.__file_path,
                  mode='w', encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        reload Method:
            Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as json_file:
                data_dict = json.load(json_file)
            for keys, values in data_dict.items():
                FileStorage.__objects[keys] = \
                            eval(values['__class__'])(**values)

        except FileNotFoundError:
            pass
