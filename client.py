# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # same as with server.py, see for expl.
    s.connect((HOST, PORT))  # connect to the server
    s.sendall(b"Hello, world")  # send this message. "b" means send in binary data format, best for socket transm.
    data = s.recv(1024)  # read server's reply

print(f"Received {data!r}")  # then print server's reply. !r means write out in string format
print(f"Connection ended.")
