def caesar_decrypt(ciphertext, shift):
    decrypted = ""

    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted += char

    return decrypted

def break_caesar_cipher(ciphertext):
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Example usage
ctxt = "Px pbee fxxm hg Fhgwtr"
break_caesar_cipher(ctxt)