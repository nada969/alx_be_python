import unittest
from simple_calculator import SimpleCalculator

class Tests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(self,5,10),15)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(self,5,10),-5)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self,5,10),50)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(self,5,10),0.5)




if __name__ == "__main__":
    unittest.main()

