#!/usr/bin/python3
#Author: MikiasHailu
""" This module Contains the TestDBStorageDocs and TestDBStorage classes """

from datetime import datetime
import inspect
import models
from models.base_model import Base
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
        "Review": Review, "State": State, "User": User}

class TestDBStorageDocs(unittest.TestCase):
    """ This class tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """ This fucntion will Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """ This function will test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")

        def test_pep8_conformance_test_db_storage(self):
            """ This fucntion will test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
                test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")

        def test_db_storage_module_docstring(self):
            """ This function will test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                "db_storage.py needs a docstring")

        def test_db_storage_class_docstring(self):
            """ This fucntion will test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                "DBStorage class needs a docstring")

        def test_dbs_func_docstrings(self):
            """ This fucntion will test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                    "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                    "{:s} method needs a docstring".format(func[0]))


            class TestDBStorage(unittest.TestCase):
                """ This class is the Test the DBStorage class"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "not testing db storage")
    def test_get(self):
        """ This fucntion will test get returns specific object """
        new_state = State(name="New York")
        new_state.save()
        new_user = User(email="bob@foobar.com", password="password")
        new_user.save()
        self.assertIs(new_state, models.storage.get("State", new_state.id))
        self.assertIs(None, models.storage.get("State", "blah"))
        self.assertIs(None, models.storage.get("blah", "blah"))
        self.assertIs(new_user, models.storage.get("User", new_user.id))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "not testing db storage")
    def test_count(self):
        """ This function will test that new adds an object to the database"""
        initial_count = models.storage.count()
        self.assertEqual(models.storage.count("Blah"), 0)
        new_state = State(name="Florida")
        new_state.save()
        new_user = User(email="bob@foobar.com", password="password")
        new_user.save()
        self.assertEqual(models.storage.count("State"), initial_count + 1)
        self.assertEqual(models.storage.count(), initial_count + 2)
