from socket import *

# 创建tcp套接字
tcp_socket = socket()

tcp_socket.connect(("127.0.0.1",9999))

while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024).decode()
    print(data)

tcp_socket.close()