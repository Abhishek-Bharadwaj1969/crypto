from pwn import *
from Crypto.Util.Padding import unpad

'''formula 
decr_block = padding_byte (xor) previous_ct (xor) control_b
''' 
def server(ct, r):
    ct = ct.hex().encode()
    r.sendline(ct)
    res = r.recvline()
    return b'Success' in res
host,port='gc1.eng.run',32001
iv = '28381f47d0097c7765468968179a722e'
iv = bytes.fromhex(iv)

def padding_oc(ct,iv=iv):
    io = remote(host,port)
    block_number = len(ct)//16
    final = b''
    for i in range(block_number, 0, -1):
        current_ct_block = ct[(i-1)*16:(i)*16]
        if(i == 1):
            prev_ct_block = iv
        else:
            prev_ct_block = ct[(i-2)*16:(i-1)*16]
        brute = prev_ct_block
        curr_plain = [0]*16 
        padding_byte = 0
        for j in range(16, 0, -1):
            padding_byte += 1
#----------------------------------------------------- Bruteforcing ---------------------------------------------------            
            for value in range(0,256):
                brute = bytearray(brute)
                brute[j-1] = value
#-------------------------- appending the control block to cipher block for decrytion ----------------------------------
                concat_blocks = bytes(brute) + current_ct_block
                if(server(concat_blocks,io)):
#----------------------------------------------------- pn[i]= 1 ⊕ cn-1[i] ⊕ c'[i] -----------------------------------
                    curr_plain[-padding_byte] = brute[-padding_byte] ^ prev_ct_block[-padding_byte] ^ padding_byte #(c'[k] is when we sent block and byte concatenated )
#------------------------------------------------------ pn[i] = 2 ⊕ cn-1[i] ⊕ c'[i] c'-->control ------------------                    
                    for p in range(1, padding_byte+1):
                        brute[-p] = padding_byte+1 ^ curr_plain[-p] ^ prev_ct_block[-p] 
                    break
        final = bytes(curr_plain) + bytes(final)
    return unpad(final,16)

iv = '28381f47d0097c7765468968179a722e'
iv = bytes.fromhex(iv)

ct = 'b573a096bf6f525498eb19d297eb95e534fd997eb03ba2a1259a22f2d4d9e4a421d6765fb3c5e26fe5aa2ba8448aa06ac229ae5e0292d3544951027ce8acb47f'
ct = bytes.fromhex(ct)

flag = poc(ct, iv)
print(flag)
```
