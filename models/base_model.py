#!/usr/bin/python3
"""
Class base model
"""
import datetime
import uuid
import json
from models import storage


class BaseModel:
    """
    first class base
    """
    def __init__(self, *args, **kwards):
        """
        starting the method
        """
        if kward:
            for key, value in kwards.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.update_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        format to print str
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        a update for the date method
        """
        self.update_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        returns a dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = dict["created_at"].isoformat()
        new_dict["updated_at"] = dict["updated_at"].isoformat()
        return new_dict
