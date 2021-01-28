# CMI Roll No - MDS202024
# Batch - MSC DS I
import string
with open("Cipher.txt","r") as f:
    text = f.read()
    with open("Key.txt","r") as k:
        key = k.read()
        with open("Message.txt","w") as m:
            for t in text:
                if t in key:
                    i = key.index(t)
                    m.write(string.ascii_uppercase[i])
                else: m.write(" ")
