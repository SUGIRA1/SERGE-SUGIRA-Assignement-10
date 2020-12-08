import unittest
import car_class
import 


# Testing The car addition ---------       TEST 1

class BasicTest(unittest.TestCase):
    def add_car(self):
        self.assertEqual(car_class.add(1, 5), 6)