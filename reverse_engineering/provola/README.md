# provola
The goal is to find the correct flag.

## Context
- The binary ask for a password (flag) which is read from `stdin`.

## Approach
By disassembling the binary we see in the main function that read from `stdin` the input that is fowarded to function check_passwork(). 
```{c}
if ( strlen(a1) != 37 ) //a1 is the input
    return 0;
  for ( i = 0; i <= 36; ++i )
  {
    shaprovola(&a1[i], 1, v4);
    for ( j = 0; j <= 31; ++j )
    {
      if ( v4[j] != provola[32 * i + j] )
        return 0;
    }
  }
  return 1;
```
- The function immediately return if the length is not 37, so we have to put exactly 37 chars to see what will happen. 
- By trial and error (and knowing the flag format is flag{}), we determined that the program returns immediately if a character is incorrect. This allows us to brute-force the flag one character at a time.
- The idea is to put a breakpoint at `++i` and run the program to run the program and check every printable character until the correct one is found (the program stops if the character is wrong).
