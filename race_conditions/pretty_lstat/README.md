# pretty_lstat

## Context
The idea is to call the win function that will read the flag. 

## Approach
The program uses `alloca` to allocate space on the stack for a file's content. However, the file's size is only checked at the beginning of execution. If the file's content changes after this initial size check, a buffer overflow can occur.

I create 3 files:
- `hello.txt`: it contains a small file "hello world!"
- `exploit.txt` used to overflow: I generate cyclic 500 into exploit.txt, then start the program in gdb passing as argument data.txt that is initialized with hello.txt. I put a bp at 0x401607 to be able to change data.txt in time. Then when the bp is hit, I change data.txt into exploit.txt, to overflow as the dimesion is higher. The program creashes with top of the stack as 'saaataaa' so the offset is 72 (bytes). Now I can call the win function by putting the address into `exploit.txt` after 72 bytes.
- `data.txt`: actual file passed to the program.

I used two terminal windows:
- Terminal 1: run the program with `data.txt` as the argument.
- Terminal 2: dynamically switch the content of `data.txt` between `hello.txt` and `exploit.txt` to execute the exploit.

By following these steps, the program executes the `win` function, allowing the flag to be read.