'''
Implement the Pollard Rho method to find a collision in the SHA256.
Assume the starting value is 0𝑥000…000
Use only 12 nibbles.
Measure the execution time.

'''

import hashlib
import time

# 24 bits = 6 hex digits
NUMBER_OF_NIBBLES = 12


# truncated sha256
def my_sha256(msg):
    hash = hashlib.sha256(msg.encode()).hexdigest()[:NUMBER_OF_NIBBLES]
    return hash


# start hash value, this H_1
h = str(0x000)
# this H`_1
h_new = h

counter = 0
start = time.time()

while True:
    h = my_sha256(h)  # H = Hash(H)
    h_new = my_sha256(my_sha256(h_new))  # H` = Hash(Hash(H`))
    counter += 1
    if h == h_new:  # a collision is detected, print the values.
        print('H_(i+1): ', h)
        print('H`_(i+1):', h_new)
        break

stop = time.time()
print('Found after', counter, 'iterations in', (stop - start), 'seconds')

