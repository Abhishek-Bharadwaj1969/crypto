# CTR(cryptopals)

1.The main modules i used here is ```struct``` and `counter` 

2.Struct: it has mainly 2 functions pack and unpack,`pack` as the name suggest it packs the values in to the format assigned so "Q" is unsigned long which returns a byte string so the format should be either little or big endian "<"=>little, "<"=>big

3.Counter is one of the  widely used  module for CTR mode implementation it returns a object which is used for passing counter in AES object 


```py

from Crypto.Cipher import AES
from Crypto.Util import Counter
from struct import *
from base64 import b64decode
key = "YELLOW SUBMARINE"
ct='L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='
ct=b64decode(ct)
#print(ct)
class nonce_and_counter:
    def __init__(self,nonce,count):
        self.nonce=nonce
        self.count=count
    def fn(self):
        iv=pack("<Q",self.nonce) #nonce
        ctr=Counter.new(64,initial_value=self.count,little_endian=True)
        self.count+=1
        total=iv+ctr()
        print(total)
        return total
def decrypt(nonce,counter,text):
	aes=AES.new(key,AES.MODE_CTR,counter=nonce_and_counter(nonce,counter).fn)
	return aes.decrypt(text)
def encrypt(nonce,counter,text):
	aes=AES.new(key,AES.MODE_CTR,counter=nonce_and_counter(nonce,counter).fn)
	return aes.encrypt(text)
nonce=0
counter=0
k=decrypt(nonce,counter,ct)
p=encrypt(nonce,counter,k)
print(k)
#f'---------------------------------------'
#print(p)
assert p == ct
#print(nonce,counter)
```
