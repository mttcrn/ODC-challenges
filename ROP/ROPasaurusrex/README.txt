main function:
  get_input();
  write(1, "Win!\n", 5);
  return 0;

get_input function:
char buff[256]; 
write(1, "Input: ", 7);
read(0, buff, 512);

there is a clear buffer overflow.

we can for read and write, since they are called in get_input.
Since there is ASRL (we do not know where is libc) we cannot call system

We want to write again on the stack, but we do not know where it is. We need to leak the address of the stack (not easy to do so).  

0x8804901b address of pop gadget
