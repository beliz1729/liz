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
        elif (32 <= (ord(k) + sp) <= 64) or (92 <= (ord(k) + sp) <= 96) or (123 <= (ord(k)+sp) <= 126):
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
        elif (32 <= (ord(k) - sp) <= 64) or (92 <= (ord(k) - sp) <= 96) or (123 <= (ord(k)-sp) <= 126):
            plaintext += chr(ord(k)+alp-sp)
        else:
            plaintext += cyphertext
    return plaintext
