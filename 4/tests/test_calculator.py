import unittest
from src.calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(15, self.calc.add(5, 10))

    def test_add_float(self):
        self.assertEqual(16, self.calc.add(5.5, 10.5))

    def test_add_minus(self):
        self.assertEqual(5, self.calc.add(-5, 10))

    def test_add_string(self):
        self.assertRaises(TypeError, self.calc.add, "five", 10)

    def test_subtract(self):
        self.assertEqual(18, self.calc.subtract(20, 2))

    def test_subtract_string(self):
        self.assertRaises(TypeError, self.calc.subtract, "twenty", 2)

    def test_multiply(self):
        self.assertEqual(10, self.calc.multiply(2, 5))

    def test_multiply_float(self):
        self.assertEqual(3, self.calc.multiply(1.5, 2))
    
    def test_multiply_minus(self):
        self.assertEqual(10, self.calc.multiply(-2, -5))

    def test_multiply_string(self):
        self.assertRaises(TypeError, self.calc.multiply, "two", 5)

    def test_divide(self):
        self.assertEqual(1, self.calc.divide(10, 10))

    def test_divide_string(self):
        self.assertRaises(TypeError, self.calc.divide, "ten", 10)

if __name__ == '__main__':
    unittest.main()