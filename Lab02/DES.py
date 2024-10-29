from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Initialize the plaintext
plaintext = b"This is a secret message!"

# Generate a secret random key of size 8 * 8 = 64 bits
key = get_random_bytes(8)

print("Plaintext: ", plaintext)
print("Key: ", key)

# Create an instance of the DES cipher. Set the mode of operation to Electronic Code Book (ECB)
des = DES.new(key, DES.MODE_ECB)

print("\n\t\t**********************************")
print("\t\t\t\t Encryption \t\t\t")
print("\t\t**********************************\n")

# The plaintext may not be multiple of 64 bits, so we have to pad it.
plaintext_padded = pad(plaintext, DES.block_size)

# Encrypt the padded plaintext
ciphertext_padded = des.encrypt(plaintext_padded)

# Print the ciphertext
print("The padded ciphertext is", ciphertext_padded)

print("\n\t\t**********************************")
print("\t\t\t\t Decryption \t\t\t")
print("\t\t**********************************\n")

# Use the same DES object and key to decrypt.
decrypted_ptxt_padded = des.decrypt(ciphertext_padded)

# Remove the padding from the decrypted ptxt
decrypted_ptxt = unpad(decrypted_ptxt_padded, DES.block_size)

print("The decrypted plaintext is", decrypted_ptxt)
