```import binascii
>>> a
'1c0111001f010100061a024b53535009181c'
>>> b
b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'
>>> c
'686974207468652062756c6c277320657965'
>>> d
b"hit the bull's eye"
>>> g=""
>>> for i in range(len(d)):
...     g+=chr(b[i]^d[i])
... 
>>> g
"the kid don't play"
>>> e=binascii.hexlify(e.encode())
>>> e
b'746865206b696420646f6e277420706c6179'
>>> e.decode()
'746865206b696420646f6e277420706c6179' 











 ```
 i did it using python shell 3
 
 


















