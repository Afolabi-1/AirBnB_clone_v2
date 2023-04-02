#!/usr/bin/python3
""" Test for the City Module """
import unittest
from models.city import City
import datetime


class TestState(unittest.TestCase):
    def setUp(self):
        self.a_inst = City()
        self.b_inst = City()
        self.b_inst.save()

    def test_setup(self):
        self.assertTrue(self.a_inst.id != self.b_inst.id)
        self.assertTrue(hasattr(self.a_inst, "updated_at"))
        self.assertTrue(hasattr(self.b_inst, "updated_at"))
        self.assertTrue(hasattr(self.a_inst, "name"))
        self.assertTrue(hasattr(self.b_inst, "name"))
        self.assertTrue(hasattr(self.a_inst, "state_id"))
        self.assertTrue(hasattr(self.b_inst, "state_id"))
        self.assertTrue(self.a_inst.created_at != self.b_inst.created_at)

    def test_types(self):
        self.assertTrue(type(self.a_inst.created_at) is datetime.datetime)
        self.assertTrue(type(self.a_inst.name) is str)

    def test_save(self):
        b_date = self.b_inst.updated_at
        self.b_inst.save()
        b_date2 = self.b_inst.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
