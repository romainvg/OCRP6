import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 8085  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(10)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection Established From : " + str(address))

    while True:     # receive data stream. it won't accept data packet greater than 1024 bytes

        cmd_send = input(' Entrer Une Commande -> ')
        conn.send(cmd_send.encode())  # send data to the client
        data = conn.recv(10240)
        if not data:      # if data is not received break
            break
        result = str(data).replace("\\r\\n", "\n")
        print("Received From Controled : " + result)

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()

