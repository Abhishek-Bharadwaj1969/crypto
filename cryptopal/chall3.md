so here we have to find the the key and the text 
so i did the same by using binascii
as for convenience i have made some functions in python
``` import binascii
st="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
def fun1(a):
	return binascii.unhexlify(a)
def xoring(a,b):
	s1=fun1(a)
	s2=fun1(b)
	s=""
	for i in range(len(s1)):
		s+=chr(s1[i]^s2[i])
	return binascii.hexlify(s.encode()).decode()
ab="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p=""
def fun2(o):
	return binascii.hexlify(o.encode())
for i in ab:
	p=xoring(st,fun2(i*len(fun1(st))))
	print(i,"--",bytearray.fromhex(p).decode())
```
so for the key X i got the text
