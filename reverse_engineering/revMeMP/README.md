# revMeMP
The goal is to find the correct flag.

## Context
- The binary takes a command-line argument (flag) and checks whether it is correct.
- Refer to [revmem](../revmem) as the approach is similar. 

## Approach
- I noticed that the program behaved differently when run under a debugger compared to normal execution. This indicated that the binary employed anti-debugging techniques.
By disassembling the binary I checked the main function:
```{c}
s1 = (char *)sub_120F(); //s1 is the input
sub_1199(a1, a2, v3);
if ( !strncmp(s1, a2[1], 0x21) )
  puts("You got the flag!");
else
  puts("Wrong!");
return 0;
```

Here it is sub_120F():
```{c}
result = ptrace(PTRACE_TRACEME, 0, 1, 0);
if ( result == -1 )
{
  puts("plz don't!");
  exit(-1);
}
```
- I hijacked the `ptrace()` syscall by making it return 0 instead of -1 so that the program could successfuly execute under the debug.

Here it is sub_1199():
```{c}
for ( i = &start; ; i = (_DWORD *)((char *)i + 1) )
{
  result = i;
  if ( i == (_DWORD *)0x1425 )
    break;
  if ( (*i & 0xF0) == 0xC0 && (*i & 0xF) == 0x0C )
  {
    puts("do not play with me!");
    exit(-1);
  }
}
return result;
```
- The binary also checks for traditional software breakpoints (int3, opcode `0xCC`). To avoid detection, I used a hardware breakpoint instead, which the program couldn’t detect as easily. The checks in `sub_1199()` seem to be specifically designed to detect the presence of the 0xCC opcode by masking different parts of the opcode and ensuring it matches the characteristics of 0xCC.
- So, I placed a hardware breakpoint just before the `strncmp()` call. By analyzing the contents of the rdi register, I was able to extract the value of s1 (flag).
