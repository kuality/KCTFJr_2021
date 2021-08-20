#! /usr/bin/python3
from pwn import *

p = remote('ctf.kuality.kr',12302)
p.recvuntil('then, can you solve the math problems with the formula?')
for i in range(3,100,2):
    print(f'{i}')
    p.recvuntil("!!\n")
    pay = '('+p.recvline()[:-1].decode().replace('*',')*(').replace('+','+')+')'
    p.sendline(str(eval(pay)))
    
p.interactive()