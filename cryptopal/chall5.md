so as the key is given we need to xor it simply with the given string
so for the first we need to convert string to bytes
and later on xor them and atlast decode the string to bytes
```import binascii
a="Burning 'em, if you ain't quick and nimbleI go crazy when I hear a cymbal"
b="ICE"
c=bytes(a.encode())
d=bytes(b.encode())*len(a)
s=""
for i in range(len(c)):
		s+=chr(c[i]^d[i])
print(binascii.hexlify(s.encode()).decode())
```
