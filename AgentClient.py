#################################################################################
#                                                                               #
#  AgentClent.py                                                                #
#                                                                               #
#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py.                                          #
#  Function:                                                                    #
#    1. Receive data of remote computer from remote computer.                   #
#        data:  Country, city, LAN IP, WAN IP, OS, User, CPU, RAM               #
#                                                                               #
#################################################################################

import socket
import subprocess
import platform


def client_program(host):
    
    port = 8085  # socket server port number
    operating_sys = platform.system()

    if operating_sys == "Windows":
        ping = subprocess.Popen(
            ["ping", "-n", "1", "-w", "10",host],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        out = str(out).replace("\\r\\n", "")
        split_received = out.split("%")
        receive = split_received[0]
        received = receive[-3]
        if received != "1":
            try:
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server
                data = ""
                head = 1
                client_socket.send(str(head).encode())
                data = client_socket.recv(1024).decode()  # receive instructions
                rcv = str(data)
            except Exception:
                rcv = "0"
        else:
            rcv = "0"

    if operating_sys == "Linux":
        ping = subprocess.Popen(
            ["ping", "-c", "1",  host],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        out = str(out).replace("\\r\\n", "")
        split_received = out.split("%")
        receive = split_received[0]
        received = receive[-1]
        if received == "0":
            try:
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server
                data = ""
                head = 1
                client_socket.send(str(head).encode())
                data = client_socket.recv(1024).decode()  # receive instructions
                rcv = str(data)
            except Exception:
                rcv = "0"
        else:
            rcv = "0"
    
    return rcv

