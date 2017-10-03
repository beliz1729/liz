def encrypt_caesar(plaintext):
    text = str(plaintext)
    cyphertext = ""
    alp = 26
    sp = 3
    for i in range(len(text)):
        k = text[i]
        if (97 <= ord(k)+sp <= 122) or (65 <= ord(k)+sp <= 90):
            cyphertext += chr(ord(k)+sp)
        else:
            cyphertext += chr(ord(k)-alp+sp)
    return cyphertext
print ('put your text here')
plaintext = input()
print ('result:', encrypt_caesar(plaintext))


def decrypt_caesar(cyphertext):
    text = str(cyphertext)
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
print ('put your text here')
cyphertext = input()
print ('result:', decrypt_caesar(cyphertext))
