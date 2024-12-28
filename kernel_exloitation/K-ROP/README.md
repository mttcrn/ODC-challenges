# k_rop
The goal is to escalate privileges to root in order to read the flag, which is stored in a file accessible only to the root user.

## Context
Here is the code for `k_rop_write`:
```{c}
memset(kernel_buffer, 0, sizeof(kernel_buffer));
copy_from_user(kernel_buffer, buffer, size);
return 0;
```
Here is the code for `k_rop_read`:
```{c}
memset(kernel_buffer, 0, sizeof(kernel_buffer));
copy_to_user(buffer, kernel_buffer, size);
return 0;
```
- Both functions reset the kernel_buffer using memset, which erases its previous contents.
- Neither function validates the size parameter, allowing a buffer overflow.
- The stack canary mitigation is bypassed, as the overflow enables direct overwriting of the return address without triggering the canary check.

## Approach 
Everything is explained in [the exploit](./exploit.c).
