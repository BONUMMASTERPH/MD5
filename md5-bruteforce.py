#usr/bin/python2.7
import time
import itertools, string
import hashlib
import sys
import signal
import threading

info = """
__________
                      .~#########%%;~.
                     /############%%;`\
                    /##/BONUMMASTER%%;,\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \.X        @#%,.@   UNDERGROUNDSEC  @#%,.@
                @#%,.@              @#%,.@
                  @#%,.@          @#%,.@
                     @#%,.@      @#%,.@
                       @#%.,@  @#%,.@
                   www.facebook.com/bonum.master
  Thanks to       :  BONUMMASTER(BONUMTEAM)-SPIDERPH
""" 
done = False
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    global done
    done=True
    sys.exit(0)
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==True:
            break
            
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    


def _attack(chrs, inputt):
    print "[+] Start Time: ", time.strftime('%H:%M:%S')
    start_time = time.time()
    t = threading.Thread(target=animate)
    t.start()
    total_pass_try=0
    for n in range(1, 31+1):
      characterstart_time = time.time()
      print "\n[!] I'm at ", n , "-character"
      
      
      for xs in itertools.product(chrs, repeat=n):

          saved = ''.join(xs)
          stringg = saved
          m = hashlib.md5()
          m.update(saved)
          total_pass_try +=1
          if m.hexdigest() == inputt:
              time.sleep(10)
              global done
              done = True

              print "\n[!] found ", stringg
              print "\n[-] End Time: ", time.strftime('%H:%M:%S')
              print "\n[-] Total Keyword attempted: ", total_pass_try
              print("\n---Md5 cracked at %s seconds ---" % (time.time() - start_time))
              sys.exit("Thank You !")

        
      print "\n[!]",n,"-character finished in %s seconds ---" % (time.time() - characterstart_time)
   


def main():
    print info
    
    inp_usr = raw_input(" add md5\n")
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    print chrs
    signal.signal(signal.SIGINT, signal_handler)
    return _attack( chrs,inp_usr );

   

if __name__ == "__main__":
    main()
   
   
   
