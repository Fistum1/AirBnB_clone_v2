#!/usr/bin/python3
"""
This module contains the TestAmenityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
#from tests.test_models.test_base_model import test_basemodel
#from models.amenity import Amenity
import pep8 as pycodestyle
import unittest
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """It tests to check the documentation and style of Amenity class"""

    @classmethod
    def setUpClass(cls):
        """It sets up for the doc tests"""

        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """It test for models/amenity.py conforms to PEP8."""

        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """It tests for tests/test_models/test_amenity.py conforms to PEP8."""

        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """It tests for the amenity.py module docstring"""

        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """It test for the Amenity class docstring"""

        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """It tests for the presence of docstrings in Amenity methods"""

        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """It tests the Amenity class"""

    def test_is_subclass(self):
        """It tests for Amenity is a subclass of BaseModel"""

        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """It tests for Amenity has attribute name, and it's as an empty string
        """

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if models.storage_t == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """It tests for to_dict method creates a dictionary with proper attrs
        """

        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """It tests for values in dict returned from to_dict are correct"""

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """It tests for the str method has the correct output"""

        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
