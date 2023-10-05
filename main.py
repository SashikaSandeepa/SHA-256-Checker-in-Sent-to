import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

# md5 = hashlib.md5()
sha256= hashlib.sha256()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        # md5.update(data)
        sha256.update(data)

print(f"File: {sys.argv[1]}")

# print("MD5: {0}".format(md5.hexdigest()))
print("SHA256: {0}".format(sha256.hexdigest()))
Given_hash = input("Enter Your Hash: ").lower().replace(" ", "")

if Given_hash == sha256.hexdigest():
    print("SHA-256 Pass")
else:
    print("SHA-256 Failed")
input()