#!/usr/bin/python3
""" Test State Module """
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Unit Tests for State Class """
    def setUp(self):
        """ Setup instances of the State Class """
        self.a_inst = State()
        self.b_inst = State()
        self.b_inst.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.a_inst.id != self.b_inst.id)
        self.assertTrue(hasattr(self.a_inst, "updated_at"))
        self.assertTrue(hasattr(self.a_inst, "name"))
        self.assertTrue(hasattr(self.b_inst, "name"))
        self.assertTrue(self.a_inst.created_at != self.b_inst.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.a_inst.created_at) is datetime.datetime)
        self.assertTrue(type(self.a_inst.name) is str)

    def test_save(self):
        """ Testing updating  """
        b_date = self.b_inst.updated_at
        self.b_inst.save()
        b_date2 = self.b_inst.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
