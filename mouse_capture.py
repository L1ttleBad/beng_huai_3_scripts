import os,time
import pyautogui as pag
while True:
    print "Press Ctrl-C to end"
    x,y = pag.position()
    pos="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    print pos
    time.sleep(0.3)
    os.system('cls')
print 'ending....'