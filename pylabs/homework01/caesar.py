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
        m = plaintext[i]
        if (97 <= ord(k)+sp <= 122) or (65 <= ord(k)+sp <= 90):
            cyphertext += chr(ord(k)+sp)
        elif (122 < (ord(m) + sp) <= 125) or (90 < (ord(m) + sp) <= 93):
            cyphertext += chr(ord(m)-alp+sp)
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
        m = cyphertext[i]
        if (97 <= ord(k)-sp <= 122) or (65 <= ord(k)-sp <= 90):
            plaintext += chr(ord(k)-sp)
        elif (94 <= (ord(m)-sp) < 97) or (62 <= (ord(m)-sp) < 65):
            plaintext += chr(ord(m)+alp-sp)
        else:
            plaintext += cyphertext
    return plaintext
