"""
Hash file is one way function (lossy) is not encryption
cannot get the original file back
"""
# library for hash
import hashlib

# show hash algor support on all platform
# print(hashlib.algorithms_guaranteed)

# How to use ?
h = hashlib.sha1()
"""
Description b"..."
 b'...' => bytes a sequence of octets (integers between 0 and 255)
 print(b'A' == b'\x41') # Result is True
 print('A' == b'A') # Result is False
 print(type(b"A"))  # Class bytes
 print(type('A')) # Class str
"""
h.update(b"Hello World") # update the hash obj with bytes concat arguments
# Example h.update(a); h.update(b); => h.update(a+b)
print(h.digest()) # return data from update
# it is result "b'\nMU\xa8\xd7x\xe5\x02/\xabp\x19w\xc5\xd8@\xbb\xc4\x86\xd0'"
print(h.digest_size) # the size result hash in bytes
print(h.block_size) # The internal block size of the hash algorithm in bytes
print(h.hexdigest()) # like digest but return hexadecimal digits


# show hash algor are available in the running Python interpreter
print(hashlib.algorithms_available)
h2 = hashlib.new("sha512")
h2.update(b"Hello World")
print(h2.digest_size) # the size result hash in bytes
print(h2.block_size) # The internal block size of the hash algorithm in bytes
print("from h2 sha512 : ",h2.hexdigest()) # like digest but return hexadecimal digits