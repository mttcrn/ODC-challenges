# cracksymb

## Context
- The binary takes the flag as input and check wheter it is correct or not.

## Approach
I disassembled the binary to analyzed its logic:
```{c}
read(0, buf, 23);
if ( check_flag(buf) )
  puts("Nope, try another one");
else
  puts("Yeah, that's my flag!");
return 0;
```
The function `check_flag` check parts of the flag and return 1 only if all of them are valid.
In the [solution](exploit.py) I used the Z3 solver to combine all the constraints, and I successfully retrieved the flag.
