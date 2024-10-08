# revmem
The goal is to find the correct flag.

## Context
- The binary takes a command-line argument (flag) and checks whether it is correct.
## Approach
By disassembling the binary we see in the main function that read from `stdin` the input that is fowarded to function check_passwork(). 
```{c}
v70 = 1;
if ( strlen(a1) != 68 ) //a1 is the input
   return 0;
//[some code omitted for clarity]
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
- Since there are a lot of `sleep()` i hijacked the syscall `nanosleep()` to make the binary faster. 
