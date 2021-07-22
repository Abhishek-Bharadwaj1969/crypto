# AES(ECB/CBC detection )[Cryptopals]


```python=
from os import urandom
import random 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key=urandom(16)
def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]
def ECB(pt,key=key):
	aes=AES.new(key,AES.MODE_ECB)
	ct=aes.encrypt(pt)
	print("ECB")
	return ct 
def CBC(pt,key=key):
	iv=key
	aes=AES.new(key,AES.MODE_CBC,iv)
	ct=aes.encrypt(pt)
	print("CBC")
	return ct 
def padding(msg):

    pad = 16-len(msg)%16
    msg+=chr(pad)*pad
    return msg
def block_detection(string):
	block=blocks(string)
	if block[0]==block[1]:
		a="AES_ECB"
	else:
		a="AES_CBC"
	print(a)
def oracle(s):
	a=get_random_bytes(random.randint(5,10)) #164*'a'
	b=get_random_bytes(random.randint(5,10)) #164*'a'
	s=a+s+b
	s=padding(s)
	k=random.randint(0,1)
	if k:
		c=ECB(s)
	else:
		c=CBC(s)
	return c 

msg='a'*60
cipher= oracle(msg)
#print(len(cipher))
detect=block_detection(cipher)



```