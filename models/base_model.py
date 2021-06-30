#!/usr/bin/python3

"""base_model.py : Creates a Class BaseModel"""
import uuid
from datetime import datetime
import models


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
        t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        # Condicion para saber si kwargs no esta vacio
        if bool(kwargs) is True:
            for keys, values in kwargs.items():
                if keys == "created_at":
                    self.__dict__[keys] = datetime.strptime(values, t)
                elif keys == "updated_at":
                    self.__dict__[keys] = datetime.strptime(values, t)
                else:
                    self.__dict__[keys] = values
        else:
            models.storage.new(self)

    def save(self):
        """
        Method that updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict
