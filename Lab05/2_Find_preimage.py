"""
This code is part of the AppliedCrypto472/672 class at UD.
The original code can be found at https://replit.com/@cgouert/cpeg472672week51?v=1#main.py
"""

import hashlib
import random
import string
import time

'''
Hash( M ) = myhash
    myhash : hash
    M : preimage
'''

NUMBER_OF_NIBBLES = 4


def random_message(size):
    """
    Generate a random message with 32 characters
    """
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return message


def find_preimage(myhash, msg_size):
    """
    Listing 6-1, page 108
    Note: make sure n_bits is "small" otherwise this will not terminate
    Average 2^n attempts to find a preimage
    """
    cnt = 0
    while True:  # repeat until you find the target hash
        M = random_message(msg_size)  # generate a random message m
        H2 = hashlib.sha256(M.encode()).hexdigest()[:NUMBER_OF_NIBBLES]  # generate the hash of m, keep last nibbles
        cnt += 1
        if myhash == H2:  # check if you found the preimage
            print('Number of tries:', cnt)
            return M


message = 'cat'
# Using SHA256
myhash = hashlib.sha256(message.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
print("Hash(", message, ") =", myhash)
print("\nFinding first and second preimages of", myhash)
print("-------------------------")
preimage = find_preimage(myhash, len(message))
while True:
    if preimage == message:
        print("Preimage found -->", preimage)
        break
    else:
        print("Second preimage found -->", preimage)
    print("*******************")

    preimage = find_preimage(myhash, len(message))
