import unittest
from simple_calculator import SimpleCalculator 

class Tests(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3),5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,10),-5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,10),50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5,10),0.5)
        
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5,0)

        self.assertRaises(ZeroDivisionError,self.calc.divide,5,0)

 
if __name__ == "__main__":
    unittest.main()
