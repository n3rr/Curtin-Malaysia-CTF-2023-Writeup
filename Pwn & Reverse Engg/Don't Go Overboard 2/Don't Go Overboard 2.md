# Don't Go Overboard 2

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/7a07f463-b7a7-4b07-bdc2-1e2f0d05c683)

## Solution

Basically this challenge is similar to Don’t Go Overboard. But this time, it checks the argument of address instead of decimal number.

So, I decompile the program using Ghidra.

Look at the main function. At line 16, it checks for address `0xf` and `0x405`.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/9832a856-4d8b-4fe0-a857-fffd1aa50dac)

The technique is still the same, find the offset which i found is 20 bytes.

So, put the address together with the payload and send it to the program like this.

`python2 -c 'print "AAAAAAAAAAAAAAAAAAAAB\x00\x00\x00\x05\x04\x00\x00\x0f"' | nc 3.26.44.175 3335`

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/50c4183c-602b-4149-9087-04e135c2bfc2)

## Flag
CURTIN_CTF{P4YL04D_0V3RF10W}
