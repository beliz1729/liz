def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    cyphertext = ""
    alp = 26
    sp = 3
    for i in range(len(plaintext)):
        k = plaintext[i]
        if (97 <= ord(k)+sp <= 122) or (65 <= ord(k)+sp <= 90):
            cyphertext += chr(ord(k)+sp)
        else:
            cyphertext += chr(ord(k)-alp+sp)
    return cyphertext


def decrypt_caesar(cyphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alp = 26
    sp = 3
    for i in range(len(cyphertext)):
        k = cyphertext[i]
        if (97 <= ord(k)-sp <= 122) or (65 <= ord(k)-sp <= 90):
            plaintext += chr(ord(k)-sp)
        else:
            plaintext += chr(ord(k)+alp-sp)
    return plaintext
