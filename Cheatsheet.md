## Cheatsheet ##
### Linux Tools ###
+ **Linux Task Manager**: `htop`
+ **Change file permissions**: `sudo chmod [+|-] [r|w|x] <file path>`
+ **Change file ownership**: `sudo chown <usr>:<group> <file path>`
+ **List errors**: `sudo dmesg` reports errors, faults and security failures
+ **Runtime info**: 
    - _pid_: `ps aux | grep  <executable>`
    - _pages map_: `sudo cat /proc/<pid>/maps` 
    - _symbols known to the kernel_: `sudo cat /proc/callsyms | grep <name of program you need>`
+ **Security check**: `checksec --file=<executable>`
+ **Change ELF libraries**:
    - make a copy of the executable `cp <old name> <new name>`
    - _loader_: `patchelf --set-interpreter ~/<...>/<new ld file> <executable>`
    - _get needed_: `patchelf --print-needed <executable>`
    - _replace needed_: `patchelf --replace-needed <old needed lib> ~/<...>/<new needed lib> <executable>`
    - _ensure positions have not been changed_: `readelf -a <patched executable> | grep main` _VS_ `readelf -a <original executable> | grep main` [if they are not the same, you have to shorten the strings locating new libraries, moving them to the excutable directory]
+ **List Dynamic Dependencies**: `ldd <executable>`
+ **List gadgets**: `ropper --nocolor -f <executable> > gadgets.txt`
+ **List of gadgets spawning a shell**: `one_gadget ./libc-<version>`

### GDB + pnwdbg ###
+ **Breakpoints**: 
    - _Set breakpoints_: `break [<function + offset> | *<address>]` or `b [<function + offset> | *<address>]`
    - _Hardware breakpoints_: `hbreak  [<function + offset> | *<address>]`
    - _Watchpoints_: `watch [<function + offset> | *<address>]` breaks when the specified location is modified
    - _Info_: `info breakpoints` shows all the set breakpoits
    - _Delete breakpoints_: `clear` deletes all breakpoints, otherwise `del <n1> <n2> ...` deletes only breakpoints n1, n2, and so on...
+ **Virtual address breakpoints**: `brva <address>` (useful for PIE binaries) 
+ **Virtual memory mapping**: `vmmap` shows each group of pages, its start and end virtual address, its size and its permissions (rwxp)
+ **Info about registers**: `info all-registers` prints all registrers content, and `info registers $<reg>` prints the content of the specified register
+ **Symbols**:
    - _Info about a symbol_: `info symbol <address>`
    - _Address of symbol_: `p &<symbol>`
    - _Content of symbol_: `p <symbol>`
+ **Print memory**: `x/<n><f> [<function> + <offset> | $<register> + <offset> | *<address> + <offset>]`, n is the number of elements to print, f is how to print (format):
    - _Hexadecimal Bytes_: `xb` or `bx`
    - _Hexadecimal half words_: `xh` or `hx` [2 Bytes, word]
    - _Hexadecimal words_: `xw` or `wx` [4 Bytes, dword]
    - _Hexadecimal giant words_: `xg` or `gx` [8 Bytes, qword]
    - _Instructions_: `i`
    - _Characters_: `c`
    - _Strings_: `s` (like chars)
+ **Stack**: `stack <len>` [len is the number of locations of the stack gdb has to print]
+ **Heap**: `heap` shows all the allocated and freed (but not reallocated) chunks
+ **Bins**: `bins` shows the dynamic list of fastbins, smallbins, largebins and the unsortedbin
+ **Change values**: `set [opt {<base type>}][$<reg> | *<addr> + <offset> | <sumbol>] = <value>`

### Kernel exploitation tools ###
+ **Unpack image**: in the same folder of the initramfs archive run `./unpack_initramfs`
+ **Pack image**: in the same folder of the initramfs archive run `./pack_initramfs`
+ **Convert a compressed Linux kernel image into an ELF**: `vmlinux-to-elf <compressed_kernel_image> <elf_kernel_name>`, in this way it is possibile to decompile it with IDA (or Ghidra)
+ **Debug with gdb**:
    - in the run.sh file add the option `-s` to enable remote connection
    - run `sudo gdb`
    - digit the command `target remote :1234`
+ **upload exploit**: in a virtualenv where there is installed pwntools, run `ipython3` and then `%run upload_exploit.py initramfs/<xploit name> <challenge>.training.offensivedefensive.it 8080 --ssl -e /home/user/exploit` 
