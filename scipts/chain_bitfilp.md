# Bitflip for 2nd block 

1. The main thing here is we use the ciphertext of the previous block as iv 
2. so if we scramble one single byte it scrambles the whole plain text and the single-byte of next plaintext block
3. our aim is to flip the byte and unscramble the plain text 
4. In this case i have taken the byte from the 2nd block and get it flipped,this results to scrambling of entire plain text of the same block 
5. so here encrypted plaintext of first block(ciphertext) will be used as iv and then we flip the byte and get the resultant o/p
6. But as said flipping the byte of iv(ciphertext e1 in this implementation) scrambles the plain text
7. so i stored the unchanged ciphertext in `k` and then bruted for the flipped character 

```py
from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad

iv=bytes(16)

key=bytes(16)

def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]

pt='Buy 1000 lots of waffles'.encode()

pt=pad(pt,16)

required = 'Buy 1000 lots of wafflee'.encode()

e1=AES.new(key,AES.MODE_CBC,iv).encrypt(blocks(pt)[0])

k=e1

a=blocks(pt)[1]

e2=AES.new(key,AES.MODE_CBC,e1).encrypt(a)

flip_byte=input(b"character given to be replaced with the flipped byte in the 2nd block"+bytes(unpad(a,16))+b":")

idx=int(input("Enter the index of byte to be flipped:"))

assert idx<=15

desired=e1[idx] ^ a[idx] ^ ord(flip_byte)

e1=e1[:idx]+bytes([desired])+e1[idx+1:]

d2=AES.new(key,AES.MODE_CBC,e1).decrypt(e2)

r=blocks(pt)[0]

for i in range(256):
	if e1[:idx]+bytes([i])+e1[idx+1:] ==k :
		p=i

original_ct=e1[:idx]+bytes([p])+e1[idx+1:]

d1=AES.new(key,AES.MODE_CBC,iv).decrypt(original_ct)

print(unpad(d1+d2,16))

```
