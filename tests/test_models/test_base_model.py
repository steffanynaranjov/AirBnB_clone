#!/usr/bin/python3
"""
unittest for base model
"""
import unittest
from models.base_model import BaseModel
import os
import models


class BaseModelTest(unittest.TestCase):
    """
    test for base model
    """

    def test_ids_maker(self):
        """
        test to generate the id
        """
        firstins = BaseModel()
        secondins = BaseModel()
        self.assertNotEqual(firstins, secondins)

    def test_docstring_mandatory(self):
        """
        docstring
        """
        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_permissions(self):
        """
        test permissions
        """
        self.assertTrue(os.access("models/base_model.py", os.X_OK))
        self.assertTrue(os.access("models/base_model.py", os.R_OK))
        self.assertTrue(os.access("models/base_model.py", os.W_OK))
        self.assertTrue(os.access("models/base_model.py", os.F_OK))

    def test_instace(self):
        """
        test instance
        """
        BaseIns = BaseModel()
        self.assertIsInstance(BaseIns, BaseModel)


if __name__ == '__main__':
    unittest.main()
