# Don't Go Overboard

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/c552da55-7029-4f8d-a5ad-ef6ea33c86da)

## Solution

For this challenge, you need to find the right offset so that it will overflow the buffer.

So, I found it at 30 bytes but it still doesn't give me the flag.

I decompile the code using Ghidra and look at the main function. 

At line 16, the program checks the argument of `0` and `5`.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/bbc456a4-77ac-4311-a8d8-af13a9cd0735)

So, I include `05` in my payload, which is 30 bytes of the letter `a`.

Like this `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa05`

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/7e80e729-e126-4d19-87b8-a9fdc6a0956e)

## Flag

CURTIN_CTF{T@RG3TT3D_0V3RF10W}
