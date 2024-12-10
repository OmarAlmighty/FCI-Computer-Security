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

NUMBER_OF_NIBBLES = 5


def random_message(msg_size):
    """
    Generate a random message with 32 characters
    """
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(msg_size)])
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


def find_collision(msg_size):
    """
    Listing 6-3, page 109
    If you can find second preimages for a hash function, you can also find collisions
    """
    M = random_message(msg_size)
    H = hashlib.sha256(M.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
    p = find_preimage(H, msg_size)
    return M, p


start_time = time.time()
m1, m2 = find_collision(32)
end_time = time.time()
h1 = hashlib.sha256(m1.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
h2 = hashlib.sha256(m2.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
print('Hash(', m1, ') =', h1)
print('Hash(', m2, ') =', h2)
print('Time:', end_time - start_time)
