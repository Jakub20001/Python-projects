import hashlib
from difflib import SequenceMatcher

def hash_file(filename1, filename2):
    
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    
    with open(filename1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
    
    with open(filename2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
            
        return h1.hexdigest(), h2.hexdigest()
    
msg1, msg2 = hash_file("D:/Downloads/pd1.pdf", "D:/Downloads/pd2.pdf")

if msg1 != msg2:
    print("These files are not identical")
else:
    print("These files are identical")
