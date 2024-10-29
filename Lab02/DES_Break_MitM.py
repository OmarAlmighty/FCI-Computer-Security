from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import itertools


def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, DES.block_size))


def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), DES.block_size)


def double_des_encrypt(key1, key2, plaintext):
    first_encryption = des_encrypt(key1, plaintext)
    return des_encrypt(key2, first_encryption)


def mitm_attack(plaintext, ciphertext, key_space):
    # Dictionary to store intermediate values
    X_key = {}

    # Encrypt plaintext with all possible keys (first encryption)
    for key1 in key_space:
        X = des_encrypt(key1, plaintext)
        X_key[X] = key1

    # Decrypt ciphertext with all possible keys (second decryption)
    for key2 in key_space:
        X = des_decrypt(key2, ciphertext)
        if X in X_key:
            return X_key[X], key2

    return None, None


def generate_key_space():
    # Generate a small key space for demonstration purposes
    key_space = []
    for key in itertools.product(range(256), repeat=8):
        key_space.append(bytes(key))

    return key_space


key1 = b'key1key1'
key2 = b'key2key2'
plaintext = b'This is a test.'

# Encrypt the plaintext using Double DES
ciphertext = double_des_encrypt(key1, key2, plaintext)

# Generate the key space
key_space = generate_key_space()

# Perform the meet-in-the-middle attack
found_key1, found_key2 = mitm_attack(plaintext, ciphertext, key_space)

if found_key1 and found_key2:
    print(f"Keys found: Key1 = {found_key1}, Key2 = {found_key2}")
else:
    print("Keys not found.")
