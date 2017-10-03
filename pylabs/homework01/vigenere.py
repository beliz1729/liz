def encrypt_vigenere(plaintext, keyword):
	text = str(plaintext)
	key = str(keyword).lower()
	cyphertext = ""
	alp = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(text)):
		wordcode = ord(text[i])
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
print ('Введите текст')
plaintext = input()
print ('Введите ключ')
keyword = input()
print ('result', encrypt_vigenere(plaintext, keyword))


def decrypt_vigenere(cyphertext, keyword):
	text = str(cyphertext)
	key = str(keyword).lower()
	plaintext = ""
	alp = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(text)):
		wordcode = ord(text[i])
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
print ('Введите текст')
cyphertext = input()
print ('Введите ключ')
keyword = input()
print ('result', decrypt_vigenere(cyphertext, keyword))