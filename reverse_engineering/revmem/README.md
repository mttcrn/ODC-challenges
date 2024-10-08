# revmem
The goal is to find the correct flag.

## Context
- The binary takes a command-line argument (flag) and checks whether it is correct.
## Approach
By disassembling the binary:
```{c}
s1 = (char *)sub_1169(a1, a2, a3); //a1 is the input passed as argument
if ( !strncmp(s1, a2[1], 30) )
  puts("You got the flag!");
else
  puts("Wrong!");
return 0;
```
- I placed a breakpoint just before the `strncmp()` call.
- By analyzing the contents of the rdi register (first argument), I was able to extract the value of s1, which corresponds to the correct flag.
