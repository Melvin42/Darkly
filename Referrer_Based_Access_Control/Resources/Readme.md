https://cs.brown.edu/courses/csci1660/wiki/attacks/Referrer-Based-Access-Control/

By clicking on the Copyright in the footer, we acces to the famous albatroz page,
when exploring the source code in the inspector, we see comments asking us to come from another site and another browser.

You must come from : "https://www.nsa.gov/".
Let's use this browser : "ft_bornToSec". It will help you a lot.

By modifiying the header with burp and a proxy, we can replace both, referer and user-agent by https://www.nsa.gov/ and ft_bornToSec
