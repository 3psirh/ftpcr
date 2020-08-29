# Help
Comand|Example                             |Description
------|------------------------------------|-------------------------------
   -p |-p *2221*                           |port
   -th|-th *20*                            |threads. Default number - 5
   -f |-f *file.txt*                       |file
   -s |-s *127.0.0.1*                      |victim's server
   
**Full Example:**

$ ftpcr.py -s 192.168.0.101 -f filewithpasswords.txt -p 2221 -th 120

***ftpcr can read only such lines:***

1. login1:password1
2. login2:password2 
3. login3:password3
