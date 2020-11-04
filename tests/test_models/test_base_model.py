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

    def test_instance(self):
        """ if is instance of BaseModel """
        test1 = BaseModel()
        self.assertIsInstance(test1, BaseModel)

    def test_basemodel_str(self):
        """
        test base model print
        """
        b = BaseModel()
        s = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(s, str(b))

    def test_basemodel_save_more_args(self):
        """
        tests to save with more arguments
        """
        with self.assertRaises(TypeError):
            BaseModel.save(self, 1, "Hello")

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
        self.assertFalse(os.access("models/base_model.py", os.X_OK))
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
