# C = P XOR K
class vernam:
    def encrption(plaintext,key2):
        en_text=""
        if len(key2)<len(plaintext):
            num=int(len(plaintext)/len(key2))
            for i in range(num):
                key=key2*num
        elif len(key2)==len(plaintext)or len(key2)>len(plaintext):
            key=key2
        for i in range(len(plaintext)):
            text=chr(ord(plaintext[i])^ord(key[i]))
            en_text+=text
        return en_text
    def decrption(cipher,key):
        return vernam.encrption(cipher,key)