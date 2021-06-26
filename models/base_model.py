#!/usr/bin/python3

"""base_model.py : Creates a Class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        Args:
            args: Non-Keyword Arguments
            kwargs: Dictorionary with arguments to set as instance attributes
        """
        # Condicion para saber si kwargs no esta vacio
        if bool(kwargs) is True:
            for keys, values in kwargs.items():
                if keys == "name":
                    self.name = values
                elif keys == "my_number":
                    self.my_number = values
                elif keys == "id":
                    self.id = values
                elif keys == "created_at":
                    self.created_at = datetime.strptime(values,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif keys == "updated_at":
                    self.updated_at = datetime.strptime(values,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.name = None
            self.my_number = None
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        Method that updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        return self.updated_at

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
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
