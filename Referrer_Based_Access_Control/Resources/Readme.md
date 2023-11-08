# Referer Based Access Control


By clicking on the Copyright in the footer, we acces to the famous albatroz page,
when exploring the source code in the inspector (or the response in burp suite), we see comments asking us to come from another site and another browser.

It deals with HTTP header fields : _referer_ and _user-agent_.

line 529:
You must come from : "https://www.nsa.gov/"

and line 782
Let's use this browser : "ft_bornToSec". It will help you a lot.

By modifiying the header with burp and a proxy, we can replace both, referer and user-agent by https://www.nsa.gov/ and ft_bornToSec

## External Resources

https://cs.brown.edu/courses/csci1660/wiki/attacks/Referrer-Based-Access-Control/