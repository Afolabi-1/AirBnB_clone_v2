#!/usr/bin/python3
""" Test State Module """
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Unit Tests for Review Class """
    def setUp(self):
        """ Setup instances of the Review Class """
        self.a_inst = Review()
        self.b_inst = Review()
        self.b_inst.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.a_inst.id != self.b_inst.id)
        self.assertTrue(hasattr(self.a_inst, "updated_at"))
        self.assertTrue(hasattr(self.a_inst, "place_id"))
        self.assertTrue(hasattr(self.b_inst, "place_id"))
        self.assertTrue(hasattr(self.a_inst, "user_id"))
        self.assertTrue(hasattr(self.b_inst, "user_id"))
        self.assertTrue(hasattr(self.a_inst, "text"))
        self.assertTrue(hasattr(self.b_inst, "text"))
        self.assertTrue(self.a_inst.created_at != self.b_inst.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.a_inst.created_at) is datetime.datetime)
        self.assertTrue(type(self.a_inst.place_id) is str)
        self.assertTrue(type(self.a_inst.user_id) is str)
        self.assertTrue(type(self.a_inst.text) is str)

    def test_save(self):
        """ Testing updating  """
        b_date = self.b_inst.updated_at
        self.b_inst.save()
        b_date2 = self.b_inst.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
