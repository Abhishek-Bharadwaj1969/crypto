# CTR implementation

```python=
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from os import urandom
from struct import *
from binascii import hexlify as hex

plain=get_random_bytes(32)

key=urandom(16)

nonce=unpack('<Q',urandom(8)) # returns a long value 



def encrypt(pt):

	ctr=Counter.new(128,initial_value=nonce[0])

	aes=AES.new(key,AES.MODE_CTR,counter=ctr)

	enc=aes.encrypt(pt)

	return enc

def decrypt(ct): # in CTR decryption also does (AES block encryption) only
 	ctr=Counter.new(128,initial_value=nonce[0])

	aes=AES.new(key,AES.MODE_CTR,counter=ctr)

	dec=aes.encrypt(ct)

	return dec

k=encrypt(plain)
print(hex(plain))
print(hex(decrypt(k)))

'''understanding of modules used 

1.struct has widely used  2 functions namely pack and unpack as the name 

suggests pack does the packing of the argument into the particular data format mentioned (for-example): the '<Q' '<'==> little endian 'Q' =>unsigned

long so the argument passed should be converted into a long value (of little endian since counter do increase after every iteration)

2. counter: it do make a counter block of number of bits assigned and make it to a callable object which is itended for the 'counter' in AES.new()'''



```