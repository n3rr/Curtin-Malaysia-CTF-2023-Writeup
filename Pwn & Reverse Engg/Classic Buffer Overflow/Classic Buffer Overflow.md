# Classic Buffer Overflow

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/e9be8818-4941-4bc9-9257-d9d047f13b4c)

## Solution

I think this is the trickiest challenge I have ever faced. 

When i run the program, it will show something like `ltrac`e or `strace` command.

I blanked for hours.. hahahah.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/36b4c1af-cce9-49ad-b25e-f5c17cf95a5c)

First of all when facing a buffer overflow challenge, find the offset which for this challenge is 40 bytes.

(Notice that `Better luck next time!` did not printed in the image below means that we hit the offset value)

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/0f10bb36-20f0-4e8e-9ad4-08f02e3e110d)

Next, I went through the code using `gdb-gef` and I found 3 functions, `main`, `getFlag` and `getInput`.

The target is the function `getFlag`, obviously to give me the flag. So, i get the address of the function which is `0x00000000004011d6` and use the same technique in challenge Don't Overboard 2.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/b5b022c8-3ed8-4ffa-9503-e342e744eef4)

So, I made a script for this.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/d570f0f4-2974-432f-a133-e2e8e7ac8db0)

Just run it and the flag is already served. Btw the shell is useless for this challenge.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/fa63de12-e29d-4a09-9f1a-78dcd8245225)

## Flag
CURTIN_CTF{B4S1C_0V3RF10W}
