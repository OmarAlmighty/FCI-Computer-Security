from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


# AES encryption and decryption function
class AES_Cipher:
    def __init__(self, key=None):
        # Generate a new random 16-byte key if no key is provided
        if key is None:
            self.key = get_random_bytes(16)  # AES key must be 16, 24, or 32 bytes long
        else:
            self.key = key

    def encrypt(self, ptxt):
        # Generate a random IV (initialization vector)
        iv = get_random_bytes(16)
        # Create AES cipher in CBC mode with the key and IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Encode the ptxt into bytes
        ptxt_encoded = ptxt.encode()

        # Pad the ptxt to be a multiple of the block size (AES block size is 16 bytes)
        padded_data = pad(ptxt_encoded, AES.block_size)

        # Encrypt the padded data
        ctxt = cipher.encrypt(padded_data)

        # Return the IV and ctxt, encoded in base64
        iv_ctxt = iv + ctxt
        return base64.b64encode(iv_ctxt).decode('utf-8')

    def decrypt(self, ctxt_base64):
        # Decode the base64-encoded ctxt
        data = base64.b64decode(ctxt_base64)

        # Extract the IV (first 16 bytes) and ctxt (rest of the data)
        iv = data[:16]
        ctxt = data[16:]

        # Create AES cipher in CBC mode with the key and IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Decrypt the ctxt
        padded_ptxt = cipher.decrypt(ctxt)

        # Remove the padding
        decrypted_data = unpad(padded_ptxt, AES.block_size)

        # Return the decrypted ptxt as a string
        return decrypted_data.decode('utf-8')


########### Fixed key ###########

# key = bytes([131] * 16)
# print(key)
# aes_cipher = AES_Cipher(key)

########### Random key ###########
aes_cipher = AES_Cipher()

# Example ptxt to encrypt
ptxt = "I love crypto classes"

print("Original ptxt:", ptxt)

# Encrypt the ptxt
encrypted = aes_cipher.encrypt(ptxt)
print("Encrypted (base64):", encrypted)

# Decrypt the ctxt back to ptxt
decrypted = aes_cipher.decrypt(encrypted)
print("Decrypted ptxt:", decrypted)
