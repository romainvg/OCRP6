import socket

s = socket.socket()
host = socket.gethostname()
port = 443

s.connect(host , port )
s.close()
