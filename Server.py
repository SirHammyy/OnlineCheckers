import asyncio
import logging
import socket

HOST = '127.0.0.1'
PORT = 12354

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", PORT))
    s.listen()
    conn1, addr1 = s.accept()
    with conn1:
        print('Connected by: ', addr1)
        data1 = conn1.recv(1024)
        print(data1)
        s.listen()
        conn2, addr2 = s.accept()
        with conn2:
            print('Connected by: ', addr2)
            data2 = conn2.recv(1024)
            print(data2)
            while True:
                print(data2)


