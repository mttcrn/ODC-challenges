# notsohandy
The goal is to find the flag.

## Context
- The binary takes the flag as argument, and check wheter it is the correct one or not.

## Approach
To understand how the binary validates the flag, I disassembled the `main` function:
```{c}
int chars_left, chars_left1, i, j, hash_val;
for ( i = 0; i < strlen(argv[1]); ++i ) {
  if ( argv[1][i] <= 64 || argv[1][i] == 127 ) {
    puts("Wrong flag!");
    return 0;
  }
}
for ( j = 0; j < strlen(argv[1]) - 4; ++j ) {
  if ( strlen(&argv[1][j]) > 4 )
    chars_left = 4;
  else
    chars_left = strlen(&argv[1][j]);
  hash_val = xhashe(&argv[1][j], chars_left, 0);
  if ( strlen(&argv[1][j]) > 4 )
    chars_left1 = 4;
  else
    chars_left1 = strlen(&argv[1][j]);
  xhashe_slow(&argv[1][j], chars_left1, 0);
  if ( hash_val != res[j] ) {
    puts("Wrong flag!");
    return 0;
  }
}
if ( j == 45 )
  puts("Correct flag!");
else
  puts("Wrong flag!");
return 0;
```
- The binary validates the `argv[1]` (flag) by hashing parts of it and comparing against an expected result (stored in `res`).
- I noticed that `xhashe_slow` is called but its result is not actually used for validation. So it is not useful to model it as it will just slow down the process.
- I implemented a solution, using symbolic execution with Z3, to automate the process of validating the flag.
