import socket

s = socket.socket()
host = socket.gethostname()
port = 8085

s.bind(('', port))
s.listen(5)


c, addr = s.accept()
print("Connexion établit à partir de" , addr )
while True:
    data = c.recv(1024).decode()
    if not data:
        break
    print(str(data))
c.close()
