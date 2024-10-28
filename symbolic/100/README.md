# 100
The goal is to find the flag.

## Context
- The binary ask for a serial as argument, if the serial is correct then it prints out the flag.

## Approach
I disassembled the binary to analyzed its logic:
```{c}
strncpy(input, argv[1], 30);
convert();
if ( check() )
  printf("flag{%s}\n", argv[1]);
else
  puts("Next time :D");
return 0;
```
- Firstly, the function `convert` maps each characters in input to their corresponding indices in a predefined set of symbols.
- The function `check` checks parts of the input and return 1 only if all of them are valid.

In the [first solution](./exploit.py) I used the z3 solver library. In the [second](./exploit1.py) and [third](./exploit.py) I used angr. 
