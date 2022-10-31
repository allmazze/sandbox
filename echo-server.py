#!/usr/bin/python3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',3000))
server.listen(4)
client_socket, address = server.accept()
with client_socket:
    while True:       
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        if not data:
            break
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        content = 'Hello, World! This is a simple echo server'.encode('utf-8')
        client_socket.send(HDRS.encode('utf-8') + content)
        print('Ready to accept new connections..')
        print()
        client_socket, address = server.accept()