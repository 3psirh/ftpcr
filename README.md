# Help
Comand|Example                             |Description
------|------------------------------------|-------------------------------
   -p |Example (-p 2221)                   |port
   -pr|Example (-p http(s);15.15.15.15:15) |proxy
   -th|Example (-th 20)                    |threads. The number of threads is 5 without this command
   
**Full Example:**

192.168.0.101 filewithpasswords.txt -p 2221 -pr http;127.0.0.1:80 -th 120

***ftpcr can read only such lines:***

1. login1:password1
2. login2:password2 
3. login3:password3
