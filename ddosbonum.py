import socket
import os
import math
import time

print('''
⸸LOGIN TO PROJECT SATAN⸸
⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸⛧⸸
''')
user = input('user:')
os.system('clear')

port = 8080
SERVER=socket.gethostbyname(socket.gethostname())
s = (f'''
WELCOME TO PROJECT SATAN
YOUR HOST:{SERVER}
[1] Methods 
[2] About
[3] Exit
''')
print(s)

while True:
 me = input(user+'>>')
 if me =='1':
   os.system('clear')
   p = ('''
   {UDP} UDPFLOOD
   {TCP} TCPFLOOD
   {OVH} OVHFRICK
   ''')
   print(p)
 if me =='UDP':
     os.system('clear')
     sh = ('''
     +----------+
     | UDP FLOOD!|
     +-----------+
     Max time: NONE
     ''')
     print(sh)
     ip = input('IP:')
     Port= input('Port:')
     Time = input('Time:')
     l = open('tt.txt','w+')
     l.write('\n1234'*int(Time))
     l.close()
     for i in range(int(Time)):
       sp =(' flooding '+ip)
       time.sleep(.5)
       print(sp)
 if me =='TCP':
   os.system('clear')
   ph = ('''
   +--------+
   |  TCP!  |
   +--------+
   max time: NONE
   ''')
   print(ph)
   pi = input('ip:')
   po = input('port:')
   tim3 = input('Time:')
   f = open('tcp.txt','w+')
   f.write('123'*int(tim3))
   for i in range(int(tim3)):
     ps = ('flooding'+pi)
     time.sleep(.5)
     print(ps)
 if me =='cls':
   os.system('clear')
   print(s)
 if me=='OVH':
   os.system('clear')
   lo = ('''
   +-----------+
   | OVH Down! |
   +-----------+
   max time NONE
   ''')
   print(lo)
   lp = input('ip:')
   prt = input('Port:')
   t1 = input('Time:')
   k = open('tm.txt','w+')
   k.write('lo'*int(t1))
   k.close()
   for i in range(int(t1)):
     print('flooding'+lp)
     time.sleep(.5)
 if me =='2':
   os.system('clear')
   print('''
                  
   --------------------
   |Made by sobakaroot|
   +------------------+

   project satan is a fake ddos tool for fun
   'cls' to clear
   ''')
   lll = input('enter')
   os.system('clear')
   print(s)
 if me =='3':
   os.system('clear')
   print('Thankyou for choosing project satan!')
   time.sleep(3)
   os.system('clear')
   quit()
