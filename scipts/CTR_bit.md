# CTR-Bitflip(cryptopals)

1.This is much more easier than CBC-Bitflip since we dont have any iv innvolved and the block-encryption is directly xored with plain text to get ciphertext and vice-versa

2.Encrypt the required payload and quote the escaping characters and do the xor and append it and decrypt it. send it to oracle or decrypt function here to get the flag or access

```python=
from Crypto.Cipher import AES
from Crypto.Util import Counter
from struct import *
from os import *
#from Crypto.Random import get_random_bytes
key=b"YELLOW SUBMARINE"
#print(key)
class nonce_and_counter:
    def __init__(self,nonce,count):
        self.nonce=nonce
        self.count=count
    def fn(self):
        iv=pack("<Q",self.nonce) #nonce
        ctr=Counter.new(64,initial_value=self.count,little_endian=True)
        self.count+=1
        total=iv+ctr()
        #print(total)
        return total
def encrypt(msg):
	msg=b"comment1=cooking%20MCs;userdate=" + msg + b";comment2=%20like%20a%20pound%20of%20bacon"
	msg=msg.replace(b"=",b"+")
	
	aes=AES.new(key,AES.MODE_CTR,counter=nonce_and_counter(nonce,counter).fn)
	return aes.encrypt(msg)

def decrypt(msg):
		
	aes=AES.new(key,AES.MODE_CTR,counter=nonce_and_counter(nonce,counter).fn)
	msg=aes.decrypt(msg)
	#print(msg)
	if b"admin=true" in msg:
		return b"): you got it"
	else:
		return b"Try again"

nonce=0
counter=0
ct=encrypt(b"admin=true")
print
#ct=ct)
#now we need to xor for required
k=((ct[37])) ^ ord("+") ^ ord("=")
ct=ct[:37]+str.encode(chr(k))+ct[38:]

print(decrypt(ct))
```
