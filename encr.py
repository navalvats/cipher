# CMI Roll No - MDS202024
# Batch - MSC DS I
import string
with open("Plain.txt","r") as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("","",string.punctuation)
    stripped = [w.translate(table) for w in words]
    text = " ".join(stripped)
    text = text.upper()
    with open("Key.txt","r") as k:
        key = k.read()
        with open("Cipher.txt","w") as c:
            for t in text:
                if t in string.ascii_uppercase:
                    i = string.ascii_uppercase.index(t)
                    c.write(key[i])
                elif t == " ":
                    c.write(" ")
            
