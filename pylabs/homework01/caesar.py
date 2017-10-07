def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("!abc123")
    '!def123'
    """
    cyphertext = ""
    alp = 26
    sp = 3
    for i in range(len(str(plaintext))):
        k = str(plaintext[i])
        if (97 <= ord(k) <= 122) or (65 <= ord(k) <= 90):
            if (97 <= ord(k)+sp <= 122) or (65 <= ord(k)+sp <= 90):
                cyphertext += chr(ord(k)+sp)
            else:
                cyphertext += chr(ord(k)-alp+sp)
        else:
            cyphertext += k
    return cyphertext


def decrypt_caesar(cyphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("!def123")
    '!abc123'
    """
    plaintext = ""
    alp = 26
    sp = 3
    for i in range(len(str(cyphertext))):
        k = str(cyphertext[i])
        if (97 <= ord(k) <= 122) or (65 <= ord(k) <= 90):
            if (97 <= ord(k)-sp <= 122) or (65 <= ord(k)-sp <= 90):
                plaintext += chr(ord(k)-sp)
            else:
                plaintext += chr(ord(k)+alp-sp)
        else:
            plaintext += k
    return plaintext
