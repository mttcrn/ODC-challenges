# open_read_write
The goal is to retrieve the flag using only open, read and write.
## context
- The shellcode is read from stdin and executed.
- The idea is to open the file ./flag, read it and write it to stdout.
## approach
- The function `open` takes as parameters the path, a flag to specify the access mode (read-only, write-only, or read/write) and a mode. It return the file descriptor.
- The function `read` takes as parameters the file descriptor, destiantion and number of bytes to read.
- The function `write` takes as parameters the file descriptor, destiantion and number of bytes to write.
I used shellcraft to generate the open-read-write shellcode.

```python
shellcode = pwnlib.shellcraft.amd64.linux.open("./flag", 0, 0)
shellcode += pwnlib.shellcraft.amd64.linux.read(3, 'rsp', 100)
shellcode += pwnlib.shellcraft.amd64.linux.write(1, 'rsp', 100)
```
3 is the first file descriptor returned from a system call that allocate a new one since 0,1,2 are already used for stdin, stout and stderr respectively.
