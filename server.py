import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created")

ip = socket.gethostbyname(socket.gethostname())
port = 5050
s.bind((ip , 5050))

s.listen(1)

print("wating for clinent")
c = socket.socket()
c , add = s.accept()
print("Connected with client" , add)

c.send(bytes("welcone to AIT ", 'utf-8'))
c.send(bytes("What is Your Query ? ", 'utf-8'))
while True:
    mes = c.recv(1024).decode('utf-8')

    if mes == 'Disconnect':
        print("client disconnected !")
        c.close()
        break
    else:
        print(mes)
        message = "SERVER :"+input()
        c.send(bytes(message,'utf-8'))

