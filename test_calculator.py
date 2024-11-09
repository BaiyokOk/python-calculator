import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class: 
    # Add test 
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    # Subtract test
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-4, -2), -2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(0, 2), -2)

    # Multiply test
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(0, 2), 0)
    
    # Divide test
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0, 6), 0)

    # Modulo test
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(0, 8), 0)

if __name__ == '__main__':
    unittest.main()