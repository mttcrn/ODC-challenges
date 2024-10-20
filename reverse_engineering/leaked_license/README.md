# leaked_license
The goal is to generate a serial code for the license 726cfc2d26c6defedb06562199f5c7d0da4f4930. 

## Context
- The binary is a license generator.

## Approach
The idea is to set license directly in the memory of the binary, so that the serial number is generated automatically.
I set a breakpoint at the start of the license generation.
```{python}
bp = d.bp(0x12C1, file="leaked_license", callback=write_license)
#[...]
def write_license(t, bp):
    print(d.memory[d.regs.rbp - OFFSET, 8].hex())
    if bp.hit_count == 1:
        d.memory[d.regs.rbp - OFFSET, 8] = int('726cfc2d00000000', base=16).to_bytes(8, byteorder="little")
    elif bp.hit_count == 2:                                
        d.memory[d.regs.rbp - OFFSET, 8] = int('26c6defe00000000', base=16).to_bytes(8, byteorder="little")
    elif bp.hit_count == 3:                                
        d.memory[d.regs.rbp - OFFSET, 8] = int('db06562100000000', base=16).to_bytes(8, byteorder="little")
    elif bp.hit_count == 4:                                
        d.memory[d.regs.rbp - OFFSET, 8] = int('99f5c7d000000000', base=16).to_bytes(8, byteorder="little")
    elif bp.hit_count == 5:                                
        d.memory[d.regs.rbp - OFFSET, 8] = int('da4f493000000000', base=16).to_bytes(8, byteorder="little")
```
By disassembling the binary I noticed that the serial number is computed one byte at time. So this breakpoint is hit 4 time, each one for each byte of the license. In doing this, I had to take into account that the memory is written in little-endian.

In this way, the serial number is automatically computed by the binary and printed in output.
