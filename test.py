import hashlib

string = 'test'

print(str(hashlib.md5(string.encode()).))