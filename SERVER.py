import socket

s = socket.socket()
host = socket.gethostname()
port = 443

s.bind(host, port)
s.listen(5)


c, addr = s.accept()
print("Connexion établit à partir de" , addr )