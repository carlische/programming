import unittest

from src.lab2.rsa import is_prime, gcd, multiplicative_inverse

class CalculatorTestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(41), True)
        self.assertEqual(is_prime(100), False)

    def test_gcd(self):
        self.assertEqual(gcd(41, 100), 1)
        self.assertEqual(gcd(100, 18), 2)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(10, 24), 5)