# slow_provola
The goal is to find the correct flag.

## Context
- The binary ask for a password (flag) which is read from `stdin`.
- Refer to [provola](../provola), since the approach is almost the same.

## Approach
By disassembling the binary I see that the input is fowarded to function check_passwork(). 
```{c}
v70 = 1;
if ( strlen(a1) != 68 ) //a1 is the input
   return 0;
//[... more code]
for ( i = 0; i <= 31; ++i )
{
  if ( v140[i] != provola[i] )
 {
    v70 = 0; //v70 is a sort of flag to check if a character is correct
    break;
  }
}
sleep(0x1B39u);
```
- The function immediately return if the length is not 68, so we have to put exactly 68.
- The consequent code repeat 68 times, one for each character.
- I hijacked the nanosleep() syscall, which is called by sleep() so I was able to make the binary run much faster, allowing for quicker brute-forcing.
- By inspecting memory addresses during execution, I noticed that each character validation was consistently spaced by an offset of 0x0A. Until a point where the offset changed. Everything can be found in [the exploit](./exploit.py).
