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
    for i in range(len(str(plaintext))):
        k = str(plaintext[i])
        if (97 <= ord(k)+sp <= 122) or (65 <= ord(k)+sp <= 90):
            cyphertext += chr(ord(k)+sp)
        elif (122 < (ord(k) + sp) <= 125) or (90 < (ord(k) + sp) <= 93):
            cyphertext += chr(ord(k)-alp+sp)
        else:
            cyphertext += plaintext
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
    for i in range(len(str(cyphertext))):
        k = str(cyphertext[i])
        if (97 <= ord(k)-sp <= 122) or (65 <= ord(k)-sp <= 90):
            plaintext += chr(ord(k)-sp)
        elif (94 <= (ord(k)-sp) < 97) or (62 <= (ord(k)-sp) < 65):
            plaintext += chr(ord(k)+alp-sp)
        else:
            plaintext += cyphertext
    return plaintext
