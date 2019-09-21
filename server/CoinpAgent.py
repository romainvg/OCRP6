#################################################################################
#                                                                               #
#  CoinpAgent.py                                                                #
#                                                                               #
#  This module is installed in computers to be managed by Remote Administrator. #
#  Function:                                                                    #
#    1. Send some of computer-informations to Remote Administrator.             #
#        information:  Country, city, LAN IP, WAN IP, OS, User, CPU, RAM        #
#    2. Server operation for Reverse Shell                                      #
#                                                                               #
#################################################################################

import os
import socket
import platform
import psutil

from urllib.request import urlopen
import json
import netifaces
import requests
import subprocess
import getpass

import cpuinfo

def server_program():

  # Getting WAN IP 
    try:
        data = json.loads(urlopen("https://ip.seeip.org/jsonip").read())
    except:
        data = json.loads(urlopen("http://ip.jsontest.com/").read())
    wan = data["ip"]
  
  # Getting CPU & User Session information 
    os = platform.system()
    if os == "Windows":
        # Getting CPU Information
        cpuin = cpuinfo.cpu.info
        cpu = cpuin[0]['ProcessorNameString']
        # Getting User Session
        user = subprocess.check_output(["WMIC", "ComputerSystem", "GET", "UserName"], universal_newlines = True)
        _, username = user.strip().rsplit("\n", 1)
        Com_user  = username.rsplit("\\", 1)
        userSession = Com_user[1]    
    if os == "Linux":
        # Getting CPU Information
        cpuin = cpuinfo.cpu.info
        cpu = cpuin[0]['model name']
        # Getting User Session
        userSession = getpass.getuser()
  
  # Getting Country & City
    ccdata = requests.get('https://ipinfo.io/'+wan+'/geo')
    content = ccdata.text
    obj = json.loads(content)
    city = obj['city']
    country = obj['country']
  
  # Getting CPU Core Number
    cpu_core = len(cpuin)
  
  # Getting RAM Size
    mem = psutil.virtual_memory()
    memory = mem.total
    
  # Getting Local IP
    interfaces = netifaces.interfaces()
    gws=netifaces.gateways()
    fg = gws['default']
    sg = fg[2]
    aa = sg[0].split('.')
    subnet = aa[0]+"."+aa[1]+"."+aa[2]
    
    UserIP = []
    ii = 0
    for i in interfaces:    
        if i == 'lo':
            continue
        iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
        if iface != None:
            for j in iface:
                UserIP.append(j['addr'])
        ii = ii+1
    for ip in UserIP:
        sub = ip.split(".")
        subip = sub[0]+"."+sub[1]+"."+sub[2]
        if subip == subnet:
            host = ip

    
  # Sending data to Client
    port = 8085  # initiate port no above 1024
    cmd_send = country + ":" + city + ":" + str(host) + "/" + str(wan) + ":" + str(userSession) + ":" + "Connected" + ":" + str(os) + ":" + str(cpu) + ":" + str(cpu_core) + ":" + str(memory)
    print(cmd_send)
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    while True:     # receive data stream. it won't accept data packet greater than 1024 bytes
        # configure how many client the server can listen simultaneously
        server_socket.listen(10)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection Established From : " + str(address))

        head = conn.recv(10240).decode()
        
        if head == "1":   # Send server informaion to GUI
            conn.send(cmd_send.encode())  # send data to the client
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if head == "2":             # Reverse shelll request Processing
            key_cmd = ""
            while key_cmd.lower().strip() != 'exit':

              key_cmd = conn.recv(1024).decode()  # receive instructions
              if key_cmd.lower().strip() != 'exit':
                  if os == "Linux":
                    if key_cmd.lower()[0:4] != 'ping':
                      num = key_cmd.split(" ")
                      if len(num) == 2:
                        if num[1] != '':
                          key_cmd = "ping -c 1 " + num[1]

                  cmd = subprocess.Popen(key_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                  cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
                  cmd_str = str(os) + str(cmd_bytes)
                  conn.send(cmd_str.encode())
                  if os == "Windows":
                    cmd_str = cmd_str.replace("\\r\\n", "\n")
                  if os == "Linux":
                    cmd_str = cmd_str.replace("\\n", "\n")
                  print('Received From Controler : ' + key_cmd)  # show in terminal
                  print('Send To Controler : ' + cmd_str)

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
