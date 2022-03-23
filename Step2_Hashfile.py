import hashlib

# file = "./filetext.txt" # path text file name
# BLOCK_SIZE = 1024 # The size of each read from the file

# file_hash = hashlib.sha1() # create obj hash sha1
# with open(file,'rb') as f: # Read file
#     fb = f.read(BLOCK_SIZE) # Read file amount blocksize
#     while len(fb) > 0: #while loop in the end file
#         file_hash.update(fb) # update hash
#         fb = f.read(BLOCK_SIZE) # read the next box

# print(file_hash.hexdigest())
# result : 8689b5d9770e71536d19eb7a4467d41d672d827a

def hash_file(filepath):
    BLOCK_SIZE = 1024
    file_hash = hashlib.sha1()
    with open(filepath,'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    # return hexa digest
    return file_hash.hexdigest()

hashfile = hash_file("./filetext.txt")
print(hashfile)