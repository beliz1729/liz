def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    key = keyword.lower()
    cyphertext = ""
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(plaintext)):
        wordcode = ord(plaintext[i])
        keycode = alp.find(key[i % len(key)])
        if (97 <= wordcode <= 122):
            if (97 <= wordcode + keycode <= 122):
                cyphertext += chr(wordcode + keycode)
            else:
                cyphertext += chr(wordcode + keycode - 26)

        if (65 <= wordcode <= 90):
            if (65 <= wordcode + keycode <= 90):
                cyphertext += chr(wordcode + keycode)
            else:
                cyphertext += chr(wordcode + keycode - 26)

    return cyphertext


def decrypt_vigenere(cyphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    key = keyword.lower()
    plaintext = ""
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(cyphertext)):
        wordcode = ord(cyphertext[i])
        keycode = alp.find(key[i % len(key)])
        if (97 <= wordcode <= 122):
            if (97 <= wordcode - keycode <= 122):
                plaintext += chr(wordcode - keycode)
            else:
                plaintext += chr(wordcode - keycode + 26)

        if (65 <= wordcode <= 90):
            if (65 <= wordcode - keycode <= 90):
                plaintext += chr(wordcode - keycode)
            else:
                plaintext += chr(wordcode - keycode + 26)
    return plaintext
