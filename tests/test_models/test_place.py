#!/usr/bin/python3
""" Test State Module """
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """ Unit Tests for Place Class """
    def setUp(self):
        """ Setup instances of the Place Class """
        self.a_inst = Place()
        self.b_inst = Place()
        self.b_inst.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.a_inst.id != self.b_inst.id)
        self.assertTrue(hasattr(self.a_inst, "updated_at"))
        self.assertTrue(hasattr(self.b_inst, "updated_at"))
        self.assertTrue(hasattr(self.a_inst, "name"))
        self.assertTrue(hasattr(self.b_inst, "name"))
        self.assertTrue(hasattr(self.a_inst, "user_id"))
        self.assertTrue(hasattr(self.b_inst, "user_id"))
        self.assertTrue(hasattr(self.a_inst, "city_id"))
        self.assertTrue(hasattr(self.b_inst, "city_id"))
        self.assertTrue(hasattr(self.a_inst, "description"))
        self.assertTrue(hasattr(self.b_inst, "description"))
        self.assertTrue(hasattr(self.a_inst, "number_rooms"))
        self.assertTrue(hasattr(self.b_inst, "number_rooms"))
        self.assertTrue(hasattr(self.a_inst, "number_bathrooms"))
        self.assertTrue(hasattr(self.b_inst, "number_bathrooms"))
        self.assertTrue(hasattr(self.a_inst, "max_guest"))
        self.assertTrue(hasattr(self.b_inst, "max_guest"))
        self.assertTrue(hasattr(self.a_inst, "price_by_night"))
        self.assertTrue(hasattr(self.b_inst, "price_by_night"))
        self.assertTrue(hasattr(self.a_inst, "latitude"))
        self.assertTrue(hasattr(self.b_inst, "longitude"))
        self.assertFalse(hasattr(self.a_inst, "amenities"))
        self.assertFalse(hasattr(self.b_inst, "amenities"))
        self.assertTrue(self.a_inst.created_at != self.b_inst.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.a_inst.created_at) is datetime.datetime)
        self.assertTrue(type(self.a_inst.name) is str)
        self.assertTrue(type(self.a_inst.number_rooms) is int)
        self.assertTrue(type(self.a_inst.number_bathrooms) is int)
        self.assertTrue(type(self.a_inst.max_guest) is int)
        self.assertTrue(type(self.a_inst.price_by_night) is int)
        self.assertTrue(type(self.a_inst.latitude) is float)
        self.assertTrue(type(self.a_inst.longitude) is float)

    def test_save(self):
        """ Testing updating  """
        b_date = self.b_inst.updated_at
        self.b_inst.save()
        b_date2 = self.b_inst.updated_at
        self.assertTrue(b_date != b_date2)

if __name__ == '__main__':
    unittest.main()
