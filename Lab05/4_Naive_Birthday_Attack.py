import hashlib
import random
import string
import time

'''
Hash( M ) = H
    H : hash
    M : preimage
'''

NUMBER_OF_NIBBLES = 10


def random_message(msg_size):
    '''
    Generate a random message with 32 characters
    '''
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(msg_size)])
    return message


def naive_birthday_attack(msg_size):
    """
    Page 110
    Steps:
        1. Compute and store 2^{n/2} random messages and hashes  <msg, hash(msg)>
        2. Sort the list based on the hashes
        3. Search the list to find two entries with the same hash
    """
    while True:
        hash_bits = NUMBER_OF_NIBBLES * 4
        hash_map = {}
        for i in range(2 ** (hash_bits // 2)):  # Step 1.
            msg = random_message(msg_size)
            h = hashlib.sha256(msg.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
            hash_map[msg] = h

        sorted_hash_map = sorted(hash_map.items(), key=lambda kv: kv[1])  # Step 2.

        for i in range(len(sorted_hash_map) - 1):  # Step 3.
            if sorted_hash_map[i][1] == sorted_hash_map[i + 1][1]:
                print('Found collision:', sorted_hash_map[i][1])
                print('\tHash(', sorted_hash_map[i][0], ') =', sorted_hash_map[i][1])
                print('\tHash(', sorted_hash_map[i + 1][0], ') =', sorted_hash_map[i + 1][1])
                return sorted_hash_map[i][0], sorted_hash_map[i + 1][0]
        print('Trying again...')  # Repeat


start_time = time.time()
m1, m2 = naive_birthday_attack(32)
end_time = time.time()
print('Execution time:', end_time - start_time)
