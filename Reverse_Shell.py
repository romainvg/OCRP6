#################################################################################
#                                                                               #
#  Reverse_Shell.py                                                             #
#                                                                               #
#  The software is licensed Creative Commons CC-BY-NC-SA. Under this agreement  #
#  you are authorized to use, share on the same rights or edit this software    #
#  for personnal purpose only. You are not allow to sell this software.         #
#                                                                               #
#    Official Website : https://coinpaign.com                                   #
#    Contact : romain.guihot@gmail.com 

#  This module is installed in Remote Administrator' computer.                  #
#  This is used in RemoteAdminTool.py. This is standalone console program       #
#  Function:                                                                    #
#    1. Reverse Shell to control remote computer                                #
#                                                                               #
#################################################################################

#--- standard package
import socket
import time
import validators

#--- dependent package
from goto import with_goto
import win32api


@with_goto
def shell_program():

    # Input Server hostname ( IP)
    label .begin
    host = input(' Enter the host ip -> ')
    
    port = 8085  # socket server port number
    client_socket = socket.socket()  # instantiate

    try:
        client_socket.connect((host, port))  # connect to the server

    except:
        print("Connection error.")
        goto .begin

    head = 2
    client_socket.send(str(head).encode())  # send head value to server
    while True:     # shell processing

        cmd_send = input(' Entrer Une Commande -> ')
        def on_exit(sig, func=None):
            print("exit")
            cmd_send = "exit"
            client_socket.send(cmd_send.encode())
            time.sleep(1000)  # so you can see the message before program exi

        win32api.SetConsoleCtrlHandler(on_exit, True)
        
        client_socket.send(cmd_send.encode())  # send shell command to server
        if cmd_send == "exit":
            break
        data = client_socket.recv(10240).decode()
        if not data:      # if data is not received, break
            break

        #--- process data received from remote computer
        sys = data.split("b")[0]
        splitdata = data.split(sys + "b")
        data = splitdata[1]
        print(sys)
        if sys == "Windows":
            result = str(data).replace("\\r\\n", "\n")
        if sys == "Linux":
            result = str(data).replace("\\n", "\n").replace("\\ ", " ").replace("\\ ", " ").replace("\\t", " ")
        print("Received From Controled : " + result)

    
    client_socket.close()  # close the connection

if __name__ == '__main__':
    shell_program()

