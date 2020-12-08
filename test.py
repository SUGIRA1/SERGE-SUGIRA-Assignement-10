from car_class import Car_class
import unittest

class MyTestCase(unittest.TestCase):

 # Testing the car price        -------------       TEST 1

    def test_car(self):
        car1 = Car_class("Benz 2xs", "2012", "2014", "RAA454Y", "AVAILABLE", 100, 0, 0)
        self.assertEqual(car1.prices, 100)


        
        
        
        
        
    if __name__ == '__main__':
    unittest.main()
