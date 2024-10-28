# prodkey
The goal is to find the flag.

## Context
- The binary takes a key as input and check wheter it is correct or not. If it is the correct one it prints out the flag. 

## Approach
I disassembled the binary to analyzed its logic:
```{c}
puts("\nPlease Enter a product key to continue: ");
fgets(s, 30, _bss_start);
if (verify_key(s)){
  stream = fopen("flag", "r");
  if (!stream){
    puts("Too bad the flag is only on the remote server!");
    return 0;
  }
  fgets(flag, 100, stream);
  printf("%s", flag);
}
return 0;
```
The function `verify_key` check parts of the key and return 1 only if all of them are valid.
In the [solution](exploit.py) I used the Z3 solver to combine all the constraints, and I successfully retrieved the flag.
