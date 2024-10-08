# crackme
The goal is to find the correct flag.

## Context
- The binary takes a command-line argument (flag) and checks whether it is correct.

## Approach
By disassembling the binary I inspected the main function:
```{c}
signal(5, catch_function);
if ( argc > 1 )
{
    input = (__int64)argv[1];
    __debugbreak();
    puts("Damn, wrong flag!");
    return 0;
 }
```
A signal handler is set up for (usually SIGTRAP in Unix-like systems), and whenever this signal is raised, the `catch_function` will be called.
When the catch_function is called, it performs an XOR-based validation on the input. The goal is to reverse this validation process and find the correct input (flag).

In [this file](/reverse.c/) I reversed the function, thus obtaining the right flag.
