from pwn import *

pairs = {(0x0804970E, 83), (0x080492A0, 17), (0x080492E5, 17), (0x08049329, 23), (0x080496AB, 24), (0x080495E4, 48), (0x0804945E, 48), (0x08049385, 54), (0x08049546, 39), (0x0804951F, 9)}

filepath = "./john_use"

# taken from the executable memory, the same for each unpacking routine
keys = [b'\x01\x02\x03\x04', b'\x10\x20\x30\x40', b'B00B', b'DEAD', b'\xff\xff\xff\xff']
base = 0x08048000

# UNPACK
for address, size in pairs:
  f = open(filepath, "rb")
  content = f.read()
  f.close()

  unpacked = b''
  offset = address - base
  k = keys[address%5]
  print(k, hex(address))
  for i in range(0, size*4, 4):
    unpacked += xor(content[offset+i : offset+i+4], k)
  
  fw = open(filepath, 'wb')
  new_content = content[:offset] + unpacked + content[offset + len(unpacked):]
  fw.write(new_content)
  fw.close()
