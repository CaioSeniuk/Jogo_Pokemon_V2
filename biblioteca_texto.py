import sys,time

def texto(str):
   for i in str + '\n':
     sys.stdout.write(i)
     sys.stdout.flush()
     time.sleep(2./100)