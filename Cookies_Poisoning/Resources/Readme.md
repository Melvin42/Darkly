# Cookie Poisoning

The Session ID cookie is used as credentials to aloow you to navigate on every page without confirm your identity on each request.
So if you can stole cookie of an existing user, you can navigate as if you were him, with same rights.
Some cookies are used to give more rights on certain user (like admin) and if we understand how it is encoded,
we can reverse it, modify it and get more privileges on the site.

Open the console and check for cookies.
There is a cookie "I am admin" with value 68934A3E9455FA72420237EB05902327
Using dcode, we found that it's value is the MD5sum of the string "false".
We just need to replace it by the MD5sum of "true":

```shell
echo -n "true" > IamAdmin && md5sum IamAdmin
b326b5062b2f0e69046810717534cb09
```

Just replace the cookie value with the new value with Burp Suite (in the repeater)

	We find a flag:
	df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

## External Resources
https://www.dcode.fr/identification-chiffrement </br>
https://www.dcode.fr/hash-md5 </br>
https://gchq.github.io/CyberChef/#recipe=MD5()
