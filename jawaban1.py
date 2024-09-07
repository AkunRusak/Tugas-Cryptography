def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Shift uppercase letters
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            # Shift lowercase letters
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Ciphertext: ONYV ONTHF
ciphertext_caesar = "ONYV ONTHF"
key_caesar = 13
decrypted_caesar = caesar_cipher(ciphertext_caesar, key_caesar)
print("Jawaban dari nomer 1 :", decrypted_caesar)
