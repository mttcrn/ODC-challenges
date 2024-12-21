# swiss

## Context
The goal is to execute the command `cat flag` which is already present in the program. In doing so we have to escape the function `blacklist`, that replace that command with another one. 

## Approach
The vulnearbility is in how the program get the command chain:
```{c}
fwrite("Enter your command chain:\n");
get_commands();
blacklist();
```
Since the function `blacklist` is called after memorizing the command, before calling it there is time to execute the chain from another terminal.

