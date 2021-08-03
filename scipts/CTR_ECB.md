# CTR using ECB

```py
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
from pwn import *
from struct import *

'''def xor(msg, key): 
	return b''.join([bytes([byte ^ key[i % len(key)]]) for i, byte in enumerate(msg)])'''

def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]

class nonce_and_counter:
    def __init__(self,nonce,count):
        self.nonce=nonce
        self.count=count
    def fn(self):
        iv=pack("<Q",nonce) #nonce
        ctr=Counter.new(64,initial_value=self.count,little_endian=True)
        self.count+=1
        total=iv+ctr()
        #print(total)
        return total
def CTR_ECB_en(pt,key,nonce,counter):
    cipher=b''
    enc=AES.new(key,AES.MODE_ECB).encrypt(nonce_and_counter(nonce,counter).fn())
    cipher+=xor(enc,blocks(pad(pt,16)))
    return cipher

def CTR_ECB_de(ct,key,nonce,counter):
    plain=b''
    dec=AES.new(key,AES.MODE_ECB).encrypt(nonce_and_counter(nonce,counter).fn())
    plain+=xor(dec,blocks(ct))
    return [plain,unpad(plain,16)]

nonce=500

ctr=0
pt=b'flag{Welcome_to_counter_i_hope_using_ECB_can_also_be_c00l}'
print(len(pt))
key=urandom(16)

ct=CTR_ECB_en(pt,key,nonce,ctr)

flag=CTR_ECB_de(ct,key,nonce,ctr)

print(flag)

```
