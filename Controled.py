import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 8085  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    data = ""

    while data.lower().strip() != 'close':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received From Server : ' + data)  # show in terminal
        if data.lower().strip() != 'close':
            message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
