# Unrestricted File Upload

The upload page accept only jpeg file.

Uplading files to website is dangerous: if the content or the extension is not checked for example, malicious
user can upload script file instead of a picture. We can also bypass some extension checks in the header:

We can upload a .php script and modify header field 'content-type' to 'image/jpeg' with BurpSuite just before sending,
or delete second extension in the request .jpeg

## External Resources
https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload
