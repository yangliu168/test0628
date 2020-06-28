'''666'''
from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)
response = "HTTP/1.1 200 OK\r\n" \
           "Content-Type:text/html\r\n" \
           "\r\n"
with open('python.html') as f:
    response += f.read()
connfd, addr = s.accept()
data=connfd.recv(1024)
connfd.send(response.encode())
