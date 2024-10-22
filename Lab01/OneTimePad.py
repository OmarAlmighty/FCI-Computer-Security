import secrets
import string

def generate_key(length):
    """Generates a random key of specified length using the secrets module."""
    return secrets.token_bytes(length)

def otp_encrypt(plaintext, key):
    """Encrypts the plaintext using the OTP method."""
    encrypted = bytearray()
    for p, k in zip(plaintext.encode(), key):
        encrypted.append(p ^ k)  # XOR operation
    return bytes(encrypted)

def otp_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the OTP method."""
    decrypted = bytearray()
    for c, k in zip(ciphertext, key):
        decrypted.append(c ^ k)  # XOR operation
    return bytes(decrypted)

# Example usage
plaintext = "This is a test message"
key = generate_key(len(plaintext))
print("Key ", key)


# Encrypting
ciphertext = otp_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypting
decrypted_text = otp_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
