# Content Missing II

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/949998e1-6e1c-4064-ab7b-a2d942767186)

## Solution

When I read the title of this question, it indicates that a content is missing. 

So I went on the website given to find a missing picture :

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/72400251-a894-44e0-9ab9-3623fc07e8c5)

What I did what inspect the source code to see the source off all these pictures 

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/bcefc7d7-09bb-42a8-8ee8-cf27c25773ed)

Then i change img src of the missing picture to `img src=”/static/Content.png”` to reveal the flag: 

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/8b6c43a6-ab6c-4e2b-a235-1cfe4c5d4f71)

## Flag

CURTIN_CTF{N33D_F0R_B3TT3R_C0D3_R3V13W}
