Looking closely to survey page we can see that url uses query with potential relative path. 
We can use that breach to access to files at the root folder of the machine like /etc/passwd

http://192.168.56.103/?page=../../../../../../../etc/passwd
