from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import itertools

# Function to perform brute force attack
def brute_force_des(ciphertext, original_plaintext):
    # create all combinations of 8 bytes, where each byte can take any value from 0 to 255.
    for key in itertools.product(range(256), repeat=8):  # Generates all possible 8-byte keys
        # Transform the key from integers to bytes.
        key_bytes = bytes(key)
        # We use try-except to handle errors occurred during decrypting when the key is incorrect
        try:
            decipher = DES.new(key_bytes, DES.MODE_ECB)  # Create a DES instance with the guessed key
            # Decrypt the ciphertext
            padded_ctxt = decipher.decrypt(ciphertext)
            # Remove the padding
            decrypted_ptxt = unpad(padded_ctxt, DES.block_size)
            print(decrypted_ptxt)
            if decrypted_ptxt == original_plaintext:
                print("Key found:", key_bytes)
                return key_bytes
        except (ValueError, KeyError):
            continue
    print("Key not found.")
    return None

# Example setup
key = b'abcdefgh'  # Original key
cipher = DES.new(key, DES.MODE_ECB)

# Data to encrypt
data = b'This is a secret message.'
padded_data = pad(data, DES.block_size)

# Encrypt the data
ciphered_data = cipher.encrypt(padded_data)

# Attempt to brute force the ciphertext
brute_force_des(ciphered_data, data)