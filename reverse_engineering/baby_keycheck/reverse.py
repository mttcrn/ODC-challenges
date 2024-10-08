import string

def brute():
    for i in range(13):
        for c in string.printable:
            if(magic0_check(c, i) == 1):
                print(c, end='')
    
    key = -0x45
    for i in range(12):
        for c in string.printable:
            if(magic1_check(c, i, key) == 1):
                print(c, end='')
                key = (key + ord(c)) % 256

def magic0_check(flag_c, i):
    magic0 = [0x1B, 0x51, 0x17, 0x2A, 0x1E, 0x4E, 0x3D, 0x10, 0x17, 0x46, 0x49, 0x14, 0x3D]
    
    key = "babuzz"
    if(ord(flag_c) ^ ord(key[i % 6]) != magic0[i]):
        return 0
    else:
        return 1

def magic1_check(flag_c, i, key):
    magic1 = [0xEB, 0x51, 0xB0, 0x13, 0x85, 0xB9, 0x1C, 0x87, 0xB8, 0x26, 0x8D, 0x7]
    
    key = (key + ord(flag_c)) % 256
    if (key != magic1[i]):
        return 0
    else:
        return 1

if __name__ == "__main__":
    print("flag{", end='')
    brute()
    print('}')
