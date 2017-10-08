# Echo client program
import socket

#HOST = '192.168.1.72'    # centos-dev
HOST = '192.168.1.67'    # u_dev
#HOST = '192.168.1.63'    # centose
PORT = 8443              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

