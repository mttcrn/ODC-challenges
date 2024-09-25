# gimme3bytes
The goal is to "pop a shell with only 3 bytes" in order to read the flag.

## Context
- The shellcode is read from `stdin`.

## Approach
The idea is to use a multistage shellcode, since we are limited in space.

In the first stage we call the syscall read in order to read the second stage from stdin.
```{asm}
    pop rdx ; pop from the stack into rdx (number of bytes to read)
    syscall
```
- `rax` register is already set to 0 (syscall number for read).
- `rdi` register is already set to 0 (fd for stdim).
- `rsi` register is already set to the buffer address. 

In the second stage, we simply pop a shell (refer to [back_to_shell](../back_to_shell/)).
- To ensure the correct execution we have to put a nopsled since the `rip` will point right after the first stage and we are writing at the beginning of the first stage. The nopsled must be at least of the dimension of the first stage.
