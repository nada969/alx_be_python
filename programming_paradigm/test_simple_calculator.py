import unittest
from simple_calculator import SimpleCalculator

class Tests(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3),5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,10),-5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,10),50)

    def test_division(self):
        self.assertEqual(self.calc.divide(5,10),0.5)




if __name__ == "__main__":
    unittest.main()