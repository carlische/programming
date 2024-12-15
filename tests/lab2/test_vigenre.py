import random
import unittest, string

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

from src.lab2 import vigenre

class CalculatorTestCase(unittest.TestCase):

    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere('Daenerys', 'AA'), 'Daenerys')
        self.assertEqual(encrypt_vigenere('Targaryen', 'a'), 'Targaryen')
        self.assertEqual(encrypt_vigenere('aaa', 'd'), 'ddd')

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere('Zmkocg', 'got'), 'Tyrion')
        self.assertEqual(decrypt_vigenere('Rogtwlzsk', 'GOT'), 'Lannister')

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = vigenre.encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))