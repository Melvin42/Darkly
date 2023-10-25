During scanning with nmap we've seen several informations:

```bash
$ nmap -p- -A -T4 192.168.56.102
```
Starting Nmap 7.94 ( https://nmap.org/ ) at 2023-10-25 16:38 CEST
Nmap scan report for 192.168.56.102
Host is up (0.0017s latency).
Not shown: 65534 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.4.6 (Ubuntu)
| http-robots.txt: 2 disallowed entries 
|_/whatever /.hidden
|_http-title: BornToSec - Web Section
|_http-server-header: nginx/1.4.6 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.57 seconds

We can see on port 80 many intels, but one of them is more interesting: .hidden

following this URL we find a lot of links, with a README file in each folder. we will need to use scrapping to be able to read every README file.

```bash
python3 scrapper.py
cat scrapFile | grep "flag"
```