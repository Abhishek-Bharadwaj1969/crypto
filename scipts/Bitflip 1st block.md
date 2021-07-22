# Bitflip 1st block 

1. Just xoring the byte required with iv and the original byte 
2. from that we get desired byte just append it and decrypt

```python=
#single block

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad

iv1=bytes(16)

key=bytes(16)

pt='Buy 1000 lots of waffles'.encode()

#required='Buy 1700 lots of waffles'.encode()

pt=pad(pt,16)

e1=AES.new(key,AES.MODE_CBC,iv1).encrypt(pt)


i=int(input("Enter the index to be flipped from pt:"))

assert i <=15

desired_byte= iv1[i] ^ pt[i] ^ ord(input("character given to be replaced with the flipped byte :"))

iv1=iv1[:i]+bytes([desired_byte])+iv1[i+1:]

d1=AES.new(key,AES.MODE_CBC,iv1).decrypt(e1)

print(unpad(d1,16))





```