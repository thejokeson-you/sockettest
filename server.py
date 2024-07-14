# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # create socket using IPv4 (AF_INET) & TCP (SOCK_STREAM)
    s.bind((HOST, PORT))  # binds this socket to a specific network interface (i.e., host) and port num
    s.listen()  # makes the server a listening socket, allows it to listen for incoming connection requests
    print(f"Server loaded. Awaiting client connection...")
    conn, addr = s.accept()  # when client connects, server calls accept() to complete/accept connection.
    # conn is new socket object to send/receive data on this connection.
    # addr is internet address of client
    with conn:   # with this new socket object... (inside here we send info)
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)    # receive from port 1024
            if not data:    # end connection if client sends blank message
                print(f"Connection ended.")
                break
            conn.sendall(data)    # echo all data sent
