import os
import sys
import socket
from _thread import *

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDR,SERVER_PORT))
server_socket.listen(10)


def threaded_server(Client):
    print(f"new Client connected...")    
    # Get the client request
    request = Client.recv(1024).decode()
    print(request)

    # Send HTTP response
    response = 'HTTP/1.1 200 OK\n\nHello World'
    Client.sendall(response.encode())
    Client.close()

def main():
    print(f"starting HTTP TCP server...")

    while True:
        Client, address = server_socket.accept()
        print(f"connected to {address[0]} and {address[1]}")
        start_new_thread(threaded_server, (Client,))

    server_socket.close()
    
if __name__ == "__main__":
    main()

# import socket


# # Define socket host and port
# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 8000

# # Create socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind((SERVER_HOST, SERVER_PORT))
# server_socket.listen(1)
# print('Listening on port %s ...' % SERVER_PORT)

# while True:    
#     # Wait for client connections
#     client_connection, client_address = server_socket.accept()

#     # Get the client request
#     request = client_connection.recv(1024).decode()
#     print(request)

#     # Send HTTP response
#     response = 'HTTP/1.0 200 OK\n\nHello World'
#     client_connection.sendall(response.encode())
#     client_connection.close()

# # Close socket
# server_socket.close()