# john_the_packer

## Context
It is taking a memory region and 4bytes at a time it is xoring it with a key (which is actually fixed).
```{c}
int __cdecl sub_804922B(int pointer_to_data, int num_value)
{
  _DWORD *copy_ptr; // eax
  int copy_num; // ecx
  int v4; // edx

  mprotect(pointer_to_data & 0xFFFFF000, 4096, 7); //protection=7 stands for 111=WRE
  copy_ptr = (_DWORD *)pointer_to_data; 
  copy_num = num_value;
  key = *(_DWORD *)*(&off_804C03C + pointer_to_data % 5);
  do
  {
    *copy_ptr++ ^= key;
    --copy_num;
  }
  while ( copy_num );
  ((void (*)(void))pointer_to_data)();
  return sub_80491E6(pointer_to_data, num_value);
}
```{c}
void __cdecl sub_80491E6(int pointer_to_data, int num_value)
{
  _DWORD *v3; // ebx
  int v4; // edx

  v3 = (_DWORD *)pointer_to_data;
  v4 = *(_DWORD *)*(&off_804C03C + pointer_to_data % 5);
  do
  {
    *v3++ ^= v4;
    --num_value;
  }
  while ( num_value );
}
```

The program is packing and unpacking itself. 

Another approach works by dumping the unpacked code each time it is unpacked into the original binary (dump memory <where to write> <start address> <end address>).

## Approach
CHECK1: it ensures that the flag starts with 'flag{'
```{c}
if ( strstr(flag, "flag{") == flag )
    return 1;
printf("wrong Header for %s\n", flag);
return 0;
```

CHECK2: it ensures that the flag end with '}'.
```{c}
if ( flag[strlen(flag) - 1] == '}' )
   return 1;
printf("wrong End for %s\n", flag);
return 0;
```

CHECK3: it ensure that the flag is made of ascii characters
```{c}
len = strlen(flag);
for ( i = 0; i < len; ++i )
{
  if ( flag[i] < 0 )
  {
    printf("Not ascii character in %s\n", flag);
    return 0;
  }
}
return 1;
```

CHECK4: it ensures that the first 6 chars of flag are 'packer'.
```{c}
for ( i = 1; i <= 6; ++i )
{
  curr_char = flag[i + 4];
  if ( curr_char != unpack_r(check_4_sub, 54, i) )
    return 0;
}
return 1;
```
which in turn calls the following `check_4_sub`:
```{c}
v6 = pow((double)param, 5.0) * 0.5166666688;
v7 = v6 - pow((double)param, 4.0) * 8.125000037;
v8 = pow((double)param, 3.0) * 45.83333358 + v7;
return (int)(float)(v8 - pow((double)param, 2.0) * 109.8750007 + (long double)param * 99.65000093 + 83.99999968);
```

CHECK5: it ensures that the following chars of flag are '-4_3-1337&-'.

CHECK6: it ensures that the last 10 chars of flag are 'annoying__'.

CHECK 7: it ensures that the flag is 33 chars long.
```{c}
return strlen(flag) == 33;
```