#!/usr/bin/python3
""" Test Amenity Module """
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """ Unit Tests for Amenity Class """
    def setUp(self):
        """ Setup instances of the Amenity Class """
        self.a_inst = Amenity()
        self.b_inst = Amenity()
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
