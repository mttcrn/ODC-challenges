# empty_spaces
The goal is to read the flag.

## Context
- The binary allows the user to write in a buffer.

## Approach
After disassembling the binary, I identified a clear buffer overflow vulnerability in the `main` function:
```{c}
char buffer[56]; 
setvbuf(stdin, 0, 2, 0);
setvbuf(stdout, 0, 2, 0);
puts("What shall we use\nTo fill the empty spaces\nWhere we used to pwn?");
read(0, buffer, 137);
empty(buffer);
```
However, the `empty` function complicates exploitation by clearing parts of the buffer:
```{c}
for ( i = 0; i <= 17; i += 4 )
    &buffer[4 * i] = 0xC3F48948;
```
This function effectively breaks the ROP chain by overwriting sections of the buffer with a specific value.

My solution exploits the fact that in `rdi` it is already present the address of buffer. By using an initial `sys_read`, I could overwrite the buffer contents with a new ROP chain that isn’t affected by the empty function's modifications.
