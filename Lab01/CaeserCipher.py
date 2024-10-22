def caesar_cipherV1(text, shift):
    result = ""
    for char in text:
        new_char = ord(char) + shift
        new_char = chr(new_char)
        result += new_char

    return result

def caesar_cipherV2(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift  - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters remain unchanged
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_cipherV1(plaintext, shift)
print(f"Encrypted: {encrypted_text}")

# # Decrypting
# decrypted_text = caesar_cipherV1(encrypted_text, -shift)
# print(f"Decrypted: {decrypted_text}")
