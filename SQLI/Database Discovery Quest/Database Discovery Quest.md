# Database Discovery Quest

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/c2d2d249-6abe-4767-9792-bb9247879511)

## Solution

For this challenge I login first to admin and go to the searchprodect page soo i need to pull out some database from the database mysql soo I use this payload and gain the flag. Payload: 123' union select database (),2,3,4,5-- -

#notes 
Before I got this payload I need to find out the row and column to get the table soo I analyze using this payload before I got retrive the flag.

`123’order by 1-- -`

I modefied the ‘1’ until theres error that’s how I got to know the column of the database 

After get this I refer to this website https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main/Error%20Based%20SQLi 

And this how find out the payload looks like..

## Flag

CURTIN_CTF{d8_@_Ba$3}
