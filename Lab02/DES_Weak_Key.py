from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Example of a known weak key (in bytes)
weak_key = b'\x01\x01\x01\x01\x01\x01\x01\x01'  # 0x01010101010101
plaintext = b'FCIL{Y0U_CR4CK3D_1T}'


# Function to perform DES encryption using a weak key
def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = des.encrypt(padded_plaintext)
    return ciphertext

# Function to perform DES decryption
def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_data = des.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size)
    return plaintext

# Encrypting the plaintext
ciphertext = des_encrypt(plaintext, weak_key)
print(f'Ciphertext: {ciphertext}')

test = b"|Y\xd3ki'\x13b\xce\x86\x0cU\xb5B\x0e}\xa9S\x05\xe9\xc5\xc6\xe7s"
# Encrypting the ciphertext again
decrypted_plaintext = des_encrypt(test, weak_key)
print(f'Decrypted Plaintext: {decrypted_plaintext}')
