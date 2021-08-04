# PCBC using ECB

```py
from Crypto.Cipher import AES
from os import urandom
from pwn import *
from binascii import hexlify as hex
pt=urandom(32)
key=urandom(16)
iv=urandom(16)
def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]
a=blocks(pt)
def encrypt(a=a,key=key,iv=iv):
    print("for 1st block of encryption")
    pt0=a[0]
    pt_xor=xor(pt0,iv)
    aes=AES.new(key,AES.MODE_ECB)
    ct0=aes.encrypt(pt_xor)
    print("for 2nd block of encryption" )
    pt1=a[1]
    pcbc_iv=xor(pt0,ct0)
    aes=AES.new(key,AES.MODE_ECB)
    pt1=xor(pt1,pcbc_iv)
    ct1=aes.encrypt(pt1)
    ct_f=ct0+ct1
    return ct_f

def decrypt(ct,key=key,iv=iv):
    print("for 1st block of decryption")
    block=blocks(ct)
    ct0=block[0]
    aes=AES.new(key,AES.MODE_ECB)
    internal=aes.decrypt(ct0)
    pt0=xor(internal,iv)
    print("for 2nd block of decryption")
    ct1=block[1]
    aes=AES.new(key,AES.MODE_ECB)
    internal1=aes.decrypt(ct1)
    pt_i=xor(ct0,pt0)
    pt_final=xor(internal1,pt_i)

    return pt0+pt_final

print(hex(pt)) # the plain text input 
ct=encrypt()
print(hex(ct))
print(hex(decrypt(ct)))
print(hex(decrypt(ct)) == hex(pt))
```
