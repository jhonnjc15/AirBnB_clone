#!/usr/bin/python3

"""base_model.py : Creates a Class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class BaseModel
    """
    def __init__(self):
        """
        Constructor
        """
        self.name = None
        self.my_number = None
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def save(self):
        """
        Method that updates the public instance attribute update_at
        """
        self.update_at = datetime.now()
        return self.update_at

    def __str__(self):
        """
        Method that returs a string
        """
        cadena = "[" + self.__class__.__name__ + "]" \
                 + " " + "(" + self.id + ")" + " " + str(self.__dict__)
        return cadena

    def to_dict(self):
        """
        Method that returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["create_at"] = self.create_at.isoformat()
        new_dict["update_at"] = self.update_at.isoformat()
        return new_dict
