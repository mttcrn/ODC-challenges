# easyrop
The goal is to read the flag.
## Context
- The binary allows the user to write in a `array`.

## Approach
After disassembling the binary, I identified a buffer overflow vulnerability in the `main` function. During each cycle, the variable controlling the index (`v3`) is incremented without validation, which allows for unintended writes outside of `array` bounds:
```{c}
int v3; 
int b; 
int a; 
int array[10]; 

*(_QWORD *)len = 839000940127;
write(1, "Try easyROP!\n", 0xD);
while ( *(__int64 *)len > 2 )
{
  *(_QWORD *)len = 0;
  *(_QWORD *)len = (int)read(0, (char *)&a, 4);
  *(_QWORD *)len += (int)read(0, (char *)&b, 4);
  v3 = i++;
  array[v3] = a + b;
  write(1, len, 4);
}
return 0;
```
My solution uses two steps:
- Firstly, I make a `sys_read` to read from stdin the string `/bin/sh` and place it into the `.bss` section of the binary (found it with IDA).
- Then, I make a ROP chain to pop a shell by executing `system("/bin/sh", 0, 0)`.
