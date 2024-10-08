# provola
The goal is to find the correct flag.

## Context
- The binary ask for a password (flag) that is read from `stdin`.

## Approach
By disassembling the binary we see in the main function that read from `stdin` the input that is fowarded to function check_passwork(). The function immediately return if the length is not 37, so we have to put exactly 37 chars to see what will happen. 
By trial and error (and knowing that the flag is in the form `flag{}`) we derived that if the a character of the psw is wrong the program will return. So we can bruteforce the flag char by char. 
