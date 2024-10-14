# leakers
The goal is to read the flag.

## Context
- The binary takes user input and echoes it back to the output.

By disassembling the binary:
```{c}
int len; 
char echostring[100]; //input
if ( mprotect((void *)((unsigned __int64)ps1 & 0xFFFFFFFFFFFFF000), 0x1000, 7) == -1 )
{
  perror("mprotect");
  exit(1);
}
puts("Welcome to Leakers!");
puts("What's your name?");
len = read(0, ps1, 100);     
if ( len > 1 && ps1[len - 1] == '\n' )
  ps1[len - 1] = 0;
```
- `mprotect` changes the memory protection of the page containing ps1, making hte memory at that location executable, writable, and readable (7 is the bitwise OR of PROT_READ, PROT_WRITE, and PROT_EXEC).
- The binary then reads up to 100 bytes into ps1 using the read system call (here we can put the shellcode).
```{c}
while (1)
{
  printf("Echo: ");
  if ( (unsigned int)read(0, echostring, 200) == 1 && (echostring[0] == '\n' || !echostring[0]) )
    break;
  printf("%s> %s", ps1, echostring);
}
```
- The buffer echostring is declared as 100 bytes, but the read call attempts to read 200 bytes into it. This is a buffer overflow vulnerability.

## Approach
- I put the shellcode into the name (basic /bin/sh shell).
- The payload overflows up to the canary's location with (0x68 + 1) bytes (to reach the canary).
- After sending the payload, the script reads the leaked canary value from the stack, which is 8 bytes long. It constructs the canary by adding a null byte (\x00) at the beginning (it usually start with a null byte).
- Another payload is sent to leak the base address of the binary. The payload length is (0x68 + 6 * 8), which overflows up to the return address. After sending this payload, the script captures the next 6 bytes, which corresponds to the address of the return pointer. The leak is then adjusted by subtracting the offset of the main function to get the base address of the binary.
- Now crafts the final payload to overwrite the return address with the address of the shellcode.
