#################################################################################
#                                                                               #
#  Port_Scan.py                                                                 #
#                                                                               #                                                                           #
#   The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement #
#   you are authorized to use, share on the same rights or edit this software   #
#   for personnal purpose only. You are not allow to sell this software.        #
#                                                                               #
#    Official Website : https://coinpaign.com                                   #
#    Contact : romain.guihot@gmail.com                                          #

#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py.                                          #
#  Function:                                                                    #
#    1. Get open port corresponding to specified IP                             #
#                                                                               #
#################################################################################

#--- standard package
import socket
import time
import threading
from queue import Queue

portdata = []
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()
q = Queue()   

tgIP = [""]

def port_scan(host):

    global portdata
    portdata = []
    target = host

    t_IP = socket.gethostbyname(target)
    tgIP.append(t_IP)
    print('Starting scan on host: ', tgIP[-1])

    startTime = time.time()
    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 9001):
        q.put(worker)

    q.join()
    print('Time taken:', time.time() - startTime)
    
    return portdata

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((tgIP[-1], port))
        with print_lock:
            text = str(port)
            portdata.append(text)
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
