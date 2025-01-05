# dynamism

## Context
The program uses dynamic code which is taken by calling an external service: it calls 3 functions `data`, `prepare_input` and `check`. 

## Approach
In order to use gdb I patched the binary with nops instead of the call to ptrace().
I put a breakpoint where the dynamic code is executed: 0x1A48 w.r.t. the binary base address. 
I reverse-engineered the assembly code.

- `data`
Content of `data` retrieved from gdb as it is passed by argument:
```
0x4827c3baaa35c7cc
0x2648a0c1cd54abaa
0x3c46afcfde54b5ab
0x3178e2e5d05ba8a5
0x3c78b7d5cd6ab2a3
0x1740a2d6cc6aa2a4
0x265ea7e5c75ab5aa
0x3c4e9cc9cb4298ed
0x35189cded854af93 
```
- `prepare_input`
It takes as input both the flag and data. It xor the input flag with the first 8 bytes of data, and put the result back into the heap at data+100. 
- `check`
It takes as input data. It checks wether the flag is correct or not, basically compares whatever is at data+8 with data+100 (result of xor of previous point), bytes by bytes.



