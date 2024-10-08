# baby_keycheck
The goal is to find the correct flag.

## Context
- The program read the input from `stdin` and check its correctness.

## Approach
By disassembling the binary I inspected the main function:
```{c}
memset(s, 0, 0x64uLL);
fwrite("flag> ", 1uLL, 6uLL, stdout);
fgets(s, 100, stdin);
puts("\n\nI'm just a crackme, nobody solves me");
if ( s[strlen(s) - 1] == '\n') 
   s[strlen(s) - 1] = 0;
if ( strncmp(s, "flag{", 5) )
  return 0;
puts("He's just a poor n00b, from a poor ctf team");
if ( s[strlen(s) - 1] != '}' )
  return 0;
puts("Spare him his life from this engineering");
```
- The input has to start with `flag{` and end with `}`.
- The input cannot exceed 100 characters.

In the next part of the code, the input undergoes two checks:
```{c}
v8 = v10; //v10 is a pointer to the stack where the input is placed (not considering the starting part 'flag{')
for ( i = 0; (unsigned int)i <= 12; ++i )
{
  if ( ((unsigned __int8)kkk[i % 6] ^ v8[i]) != magic0[i] )
    return 0;
}
//[... omitted not relevant code]
```
The first 13 characters (after "flag{") are XORed with values from `kkk`, then compared to `magic0`.

```{c}
v8 += 13; //the pointer is incremented by 13 positions, the ones already checked with the previous function
v4 = -69; 
for ( j = 0; j <= 11; ++j )
{
  v4 += *v8++;
  if ( v4 != magic1[j] )
    return 0;
}
//[... omitted not relevant code]
puts("Your input looks like the correct flag \\(^o^)/");
```
The next 12 characters undergo an accumulation check with `magic1`.
- By inspecting the bynary's memory in IDA I extracted the values of `magic0`, `kkk` and `magic1`.
In [this file](/reverse.py/) I reversed the two functions, thus obtaining the right flag.
