# baby_kernel
The goal is to escalate privileges to root in order to read the flag, which is stored in a file accessible only to the root user.

## Context
The function `baby_kernel_ioctl` is in charge of the input/output control. It will be called with an ioctl syscall is performed on the fd of the related kernel module. 
Here is the code:
```{c}
if ( cmd != 1337 ) \\ if the command is 1337 
    return -22;
arg(); \\ it perform a function call to the third parameter
return 0;
```
The point of the challenge is to put a shellcode in userspace and call it with this function.

## Approach
Everything can be found in [the exploit](./exploit.c).
