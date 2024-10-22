# 100
The goal is to find the flag.

## Context
- The binary ask for a serial as argument, if the serial is correct then it prints out the flag.

## Approach
In the first [exploit](./exploit.py) I used the z3 solver library, but it takes lot of time.
In the second [exploit](./exploit1.py) I used angr, to insert into the memory the symbolic value. 
