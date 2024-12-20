def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    i = 0
    for char in plaintext:
        if 'A' <= keyword[i % len(keyword)] <= 'Z':
            shift = ord(keyword[i % len(keyword)]) - ord('A')
        else:
            shift = ord(keyword[i % len(keyword)]) - ord('a')
        if 'A' <= char <= 'Z':
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
        i += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    i = 0
    for char in ciphertext:
        if 'A' <= keyword[i % len(keyword)] <= 'Z':
            shift = ord(keyword[i % len(keyword)]) - ord('A')
        else:
            shift = ord(keyword[i % len(keyword)]) - ord('a')
        if 'A' <= char <= 'Z':
            plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
        i += 1
    return plaintext