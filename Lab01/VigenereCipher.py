def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        # Get the next key index
        key_index  = key_index % key_length
        # Get the letter at that index
        k = key[key_index]
        # compute the shift amount
        shift = ord(k.lower()) - ord('a')
        if mode == 'decrypt':
            shift = -shift

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            key_index += 1
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
            key_index += 1
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result


# Example usage
plaintext = "THEY DRINK THE TEA"
keyword = "DUH"
encrypted_text = vigenere_cipher(plaintext, keyword, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

decrypted_text = vigenere_cipher(encrypted_text, keyword, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
