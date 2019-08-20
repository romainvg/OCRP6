import socket
import time
import platform
from datetime import datetime


def check_internet():
    try:
        r = request.get('https://google.com')
        print('\033[1;92[\033[1;49m+\033[1,92m] Internet Found !')
    except:
        print('\033[1;92[\033[1;49m+\033[1,92m] Internet Not Found')


def portscanner(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        print('\033[1;92[\033[1;49m+\033[1,92m] Port '+str(port)+' Open!' )
    except:
        #pass
        print('\033[1;92[\033[1;49m+\033[1,92m] Port '+str(port)+' \033[1;91mclosed !')



def main():
    check_internet()
    os.system('clear')
    os.system('clear')
    target = raw_input('\033[1;92[\033[1;49m+\033[1,92m] Enter Target IP :> ')
    x = raw_input('\033[1;92[\033[1;49m+\033[1,92m] Enter Max Port :> ')
    i = 1
    y = 1
    t = datetime.now().strftime('[%H:%M%S]')
    print('\033[1;92[\033[1;49m+\033[1,92m] Scanner Started At '+str(t))

    while i<x:

        thread.start_new_thread(portscanner, (target, y))
        time.sleep(0.1)
        i = i+1
        y = y+1

    print('\033[1;92[\033[1;49m+\033[1,92m] Scanner Finished !')


main()

