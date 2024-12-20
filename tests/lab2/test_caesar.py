import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('axbkbovp'), 'daenerys')
        self.assertEqual(encrypt_caesar('qxodxovbk'), 'targaryen')
        self.assertEqual(encrypt_caesar('qxodxovbk'), 'targaryen')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('ydodu_prujkxolv'), 'valar_morghulis')
        self.assertEqual(decrypt_caesar('ydodu_grkdhulv'), 'valar_dohaeris')