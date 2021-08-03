# CBC using ECB

```py
from Crypto.Cipher import AES
from os import urandom
from pwn import *
pt=urandom(32)
key=urandom(16)
iv=urandom(16)
def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]
a=blocks(pt)
pt0=a[0]
pt1=a[1]
pt0=xor(pt0,iv)
aes=AES.new(key,AES.MODE_ECB)
ct0=aes.encrypt(pt0)
aes=AES.new(key,AES.MODE_ECB)
pt1=xor(pt1,ct0)
ct1=aes.encrypt(pt1)
ct_f=ct0+ct1
ct_c=AES.new(key,AES.MODE_CBC,iv)
ct_c=ct_c.encrypt(pt)
print(ct_c == ct_f) # implemented CBC using ECB



```
