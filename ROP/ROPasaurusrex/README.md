# ROPasaurusrex

## Context
In the `get_input()` function there is a clear buffer overflow:
```{c}
  char buff[256]; 
  write(1, "Input: ", 7);
  read(0, buff, 512);
```
This allows to overwrite the return address with a ropchain.
We can for sure call `read` and `write`, since they are called in `get_input`.
Since there is ASRL (we do not know where is libc) we cannot call `system`.

## Approach
1st part: leak the LIBC base address
- I fill the buffer until the return address, where I put the address of `write@plt` passing as arguments: 1 (std output), the GOT entry of read and the size of an adress (take into account that it is a 32-bit challenge).
- After the write function I put the return address to `main` so that it will restart the program.
- At this point I got the leak of `read@plt`.

2nd part: call `system("/bin/sh")`
- I fill the buffer until the return address, where I put the address of `read` in LIBC passing as arguments: 0 (std input), the address where `/bin/sh` will be stored (0x804c300) and the number of bytes in the string `/bin/sh` to be read (7).
- Call system with the appropriate arguments.
