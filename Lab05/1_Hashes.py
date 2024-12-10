import hashlib

message1 = b"I Love Crypto. "
message2 = b"Hash algorithms are important"

##############################################
"""
MD5
"""
print("############### MD5 ################")
h1 = hashlib.md5(message1)
h2 = hashlib.md5(message2)
h3 = hashlib.md5(message1 + message2)
print("MD5(", message1, ") =", h1.hexdigest())
print("MD5(", message2, ") =", h2.hexdigest())
print("MD5(", message1 + message2, ") =", h3.hexdigest())
md5 = hashlib.md5()
md5.update(message1)
md5.update(message2)
print("Using update() =", md5.hexdigest())
print()
################################################
"""
SHA-1
"""
print("############### SHA-1 ################")
h1 = hashlib.sha1(message1)
h2 = hashlib.sha1(message2)
h3 = hashlib.sha1(message1 + message2)
print("SHA-1(", message1, ") =", h1.hexdigest())
print("SHA-1(", message2, ") =", h2.hexdigest())
print("SHA-1(", message1 + message2, ") =", h3.hexdigest())
sha1 = hashlib.sha1()
sha1.update(message1)
sha1.update(message2)
print("Using update() =", sha1.hexdigest())
print()
################################################
"""
SHA-256
"""
print("############### SHA-256 ################")
h1 = hashlib.sha256(message1)
h2 = hashlib.sha256(message2)
h3 = hashlib.sha256(message1 + message2)
print("SHA-256(", message1, ") =", h1.hexdigest())
print("SHA-256(", message2, ") =", h2.hexdigest())
print("SHA-256(", message1 + message2, ") =", h3.hexdigest())
sha256 = hashlib.sha256()
sha256.update(message1)
sha256.update(message2)
print("Using update() =", sha256.hexdigest())
print()
################################################
"""
SHA3-512
"""
print("############### SHA3-512 ################")
h1 = hashlib.sha3_512(message1)
h2 = hashlib.sha3_512(message2)
h3 = hashlib.sha3_512(message1 + message2)
print("SHA3-512(", message1, ") =", h1.hexdigest())
print("SHA3-512(", message2, ") =", h2.hexdigest())
print("SHA3-512(", message1 + message2, ") =", h3.hexdigest())
sha3_512 = hashlib.sha3_512()
sha3_512.update(message1)
sha3_512.update(message2)
print("Using update() =", sha3_512.hexdigest())
print()
################################################
"""
BLAKE2b, optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes
"""
print("############### BLAKE2b ################")
h1 = hashlib.blake2b(message1)
h2 = hashlib.blake2b(message2)
h3 = hashlib.blake2b(message1 + message2)
print("blake2b(", message1, ") =", h1.hexdigest())
print("blake2b(", message2, ") =", h2.hexdigest())
print("blake2b(", message1 + message2, ") =", h3.hexdigest())
blake2b = hashlib.blake2b()
blake2b.update(message1)
blake2b.update(message2)
print("Using update() =", blake2b.hexdigest())
print()
################################################
"""
BLAKE2s, optimized for 8- to 32-bit platforms and produces digests of any size between 1 and 32 bytes.
"""
print("############### BLAKE2s ################")
h1 = hashlib.blake2s(message1)
h2 = hashlib.blake2s(message2)
h3 = hashlib.blake2s(message1 + message2)
print("blake2s(", message1, ") =", h1.hexdigest())
print("blake2s(", message2, ") =", h2.hexdigest())
print("blake2s(", message1 + message2, ") =", h3.hexdigest())
blake2s = hashlib.blake2s()
blake2s.update(message1)
blake2s.update(message2)
print("Using update() =", blake2s.hexdigest())
print()
