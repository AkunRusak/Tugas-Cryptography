def vigenere_cipher(text, key, decrypt=True):
    result = ""
    key = key.upper()
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_index = ord(key[i % key_length]) - 65
            if decrypt:
                if char.isupper():
                    result += chr((ord(char) - 65 - key_index) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - key_index) % 26 + 97)
            else:
                if char.isupper():
                    result += chr((ord(char) - 65 + key_index) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + key_index) % 26 + 97)
        else:
            result += char
    return result

# Soal: JRHTOIWNB SO
ciphertext_vigenere = "JRHTOIWNB SO"
key_vigenere = "BEEF"
decrypted_vigenere = vigenere_cipher(ciphertext_vigenere, key_vigenere)
print("Jawaban dari Nomer 2 :", decrypted_vigenere)
