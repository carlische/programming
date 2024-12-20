import unittest

from src.lab1.calculator import addition, subtraction, multiplication, division

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(100, 22), 122)
        self.assertEqual(addition(123, 98), 221)

    def test_subtraction(self):
        self.assertEqual(subtraction(34, 34), 0)
        self.assertEqual(subtraction(78, 100), -22)

    def test_multiplication(self):
        self.assertEqual(multiplication(12, 10), 120)
        self.assertEqual(multiplication(0, 345), 0)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)
        self.assertEqual(division(987, 0), "Error: division by zero")