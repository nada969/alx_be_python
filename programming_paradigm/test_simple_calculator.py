import unittest
from simple_calculator import SimpleCalculator

class Tests(unittest.TestCase):
    def setUp(self):
        self.cal = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3),5)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(5,10),-5)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(5,10),50)

    def test_divide(self):
        self.assertEqual(self.cal.divide(5,10),0.5)




if __name__ == "__main__":
    unittest.main()

