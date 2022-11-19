import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))


s.send(b'Hola desde el Cliente!')
data = s.recv(1024) #Bits
print('Recibir mensaje del servidor: {0}'.format(data.decode()))


s.close()
