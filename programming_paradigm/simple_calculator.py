# simple_calculator.py
import unittest

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
    

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


else:
    print("nooo")