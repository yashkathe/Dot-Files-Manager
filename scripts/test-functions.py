import hashlib
import os

def get_file_hash(filepath):
    hasher = hashlib.sha256() 
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):  
            hasher.update(chunk)
    return hasher.hexdigest()

file1 = "/home/yashkathe/f1.txt"
file2 = "/home/yashkathe/f2.txt"

print(os.path.exists(file1))
print(os.path.exists(file2))

if get_file_hash(file1) == get_file_hash(file2):
    print("Files are the same")
else:
    print("Files are different")
