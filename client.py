import socket

c = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port = 5050
c.connect((ip,5050))

print(c.recv(1024).decode())
print(c.recv(1024).decode())

while True:
    mes = "Client : "+input("Answer to SERVER :")
    if mes == 'Client : disconnect':
        c.send(bytes("Disconnect", 'utf-8'))
    else:
           c.send(bytes(mes, 'utf-8'))
           print(c.recv(1024).decode())

