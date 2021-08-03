# CBC-Bitflip(cryptopals)

```python=
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
def blocks(array):
    return [array[i:i+16] for i in range(0, len(array), 16)]
key="YELLOW SUBMARINE"
iv="Hello_iam_abhi::"
def CBC_encrypt(msg):
	msg="comment1=cooking%20MCs;userdate=" + msg + ";comment2=%20like%20a%20pound%20of%20bacon"
	msg=msg.replace("=","+")
	msg=msg.replace(";","-")
	#padding
	pad=16-len(msg)%16
	msg+=chr(pad)*pad
	aes=AES.new(key,AES.MODE_CBC,iv)
	cipher=aes.encrypt(msg)
	return cipher

def CBC_decrypt(msg): #cipher
	#key="YELLOW SUBMARINE"
	#iv="Hello_iam_abhi::"
	aes=AES.new(key,AES.MODE_CBC,iv)
	plain=aes.decrypt(msg)
	print(unpad(plain,16))
	if ";admin=true;" in plain:
		print (":)you_got_it ")
	else:
		print("lol be admin first")
def Bitflip(msg):
	a=[]
	cipher=CBC_encrypt(msg)
	a=blocks(cipher)
	b=list(a[1])
	print(len(a))
	b[0]=chr(ord(b[0])^ord("-") ^ ord(";"))
	b[6]=chr(ord(b[6])^ord("+") ^ ord("="))
	b[11]=chr(ord(b[11])^ord("-") ^ ord(";"))
	a[1]="".join(b)
	k=CBC_decrypt(''.join(a))
	return a


req_string=";admin=true;"
Bitflip(req_string)
```
