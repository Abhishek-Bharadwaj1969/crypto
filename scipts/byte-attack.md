# ECB-Byte-Attack(Easy)

## Approach : 
1. so initially we need to find the length of block which was `flag_length()` function
2. for suppose our flag length is 44 i.e 32+12 and we need to attack bascially for those remaining bytes which was done at `required_blocks()` 
3. just simulate the byte-atack scenerio to get the required 
```python=
from Crypto.Cipher import AES
from string import printable
from base64 import b64decode
secret=str(b64decode('''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''))
Block_size=16
def flag_length():
    l1=len(one('a'))
    for i in range(2,17):
        l2=len(one(i*'a'))
        #print(i,l2)
        if l2-l1==16:
            flag_length=len(one((i-1)*'a'))-i
            break
    return flag_length

def required_blocks(): #remainig bytes 
	a=flag_length()
	b=a//16
	c=a- (16*b)	
	return c 


def padding(msg):

    pad = 16-len(msg)%16
    msg+=chr(pad)*pad
    return msg

def one(plain,secret=secret):

	msg=plain + secret
	p=padding(msg)
	key="YELLOW SUBMARINE"
	a=AES.new(key,AES.MODE_ECB).encrypt(p)
	#print(a)
	return a
#print(len((one('a'*15))))
#finding length
def exploit():
	l=required_blocks()
	flag=""
	for p in range(1,l):
		for i in range(1,17):
			mess='a'*(16-i)
			a=one(mess)
			a=a[:16*p]
			for c in range(256):
				b=one(mess+flag+chr(c))
				b=b[:16*(p)]
				if padding(a) == padding(b):
					flag+=chr(c)
					break	
					

	return flag


print(exploit())

```
