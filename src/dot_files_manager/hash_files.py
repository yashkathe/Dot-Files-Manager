import hashlib

# hash file with sha256 
def get_file_hash(filepath):

    hasher = hashlib.sha256()
    
    with open(filepath, "rb") as f:
    
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    
    return hasher.hexdigest()

# check if files are similar based on hashing 
def are_similar_files(f1, f2):
    
    if get_file_hash(f1) == get_file_hash(f2):
        return True
    
    else:
        return False
