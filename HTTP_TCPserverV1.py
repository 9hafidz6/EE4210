# import os
# import sys
# import socket
# from _thread import *

# SERVER_ADDR = '127.0.0.1'
# SERVER_PORT = 4322

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((SERVER_ADDR,SERVER_PORT))
# server_socket.listen(10)


# def threaded_server(Client):
#     print(f"new Client connected...")    
#     # Get the client request
#     request = Client.recv(1024).decode()
#     print(request)

#     # Send HTTP response
#     response = '''HTTP/1.1 200 OK\n\n
#                         <html>
#                         <form action="/127.0.0.1:4321" method="GET">
#                         <ul>
#                         <li>
#                             <label for="text">Input:</label>
#                             <input type="text" id="name" name="response">
#                         </li>
#                         <li class="button">
#                         <button type="submit">Send your input</button>
#                         </li>
#                         </ul>
#                         </form>
#                         </html>'''
#     Client.sendall(response.encode())
#     # Client.sendall(" ".encode())
#     request = Client.recv(1024).decode()
#     Client.close()

# def main():
#     print(f"starting HTTP TCP server...")

#     # while True:
#     #     Client, address = server_socket.accept()
#     #     print(f"connected to {address[0]} and {address[1]}")
#     #     start_new_thread(threaded_server, (Client,))
#     Client, address = server_socket.accept()
#     print(f"connected to {address[0]} and {address[1]}")
#     threaded_server(Client)

#     server_socket.close()
    
# if __name__ == "__main__":
#     main()

#========================================================================================================================

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

#========================================================================================================================

import os
import socket
import time
import re

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 4320
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDR,SERVER_PORT))
server_socket.listen(10)

# COUNT = 1

def handle_client(server_socket, addr, i):
    COUNT=1
    while True:
        data=server_socket.recv(1024).decode()
        data = data.splitlines()
        # decoded_data=data.decode("utf-8")
        if not data:
            print(f"this is the received data from client {i}: {data}")
            server_socket.close()
            break
        if COUNT == 1:
            print("CLIENT " + str(i) + " -> " + data[0])
            response = '''HTTP/1.1 200 OK\n\n
                            <html>
                            <form action="127.0.0.1:4321" method="GET">
                            <ul>
                            <li>
                                <label for="text">Input:</label>
                                <input type="text" id="name" name="response">
                            </li>
                            <li class="button">
                            <button type="submit">Send your input</button>
                            </li>
                            </ul>
                            </form>
                            </html>'''
            server_socket.sendall(response.encode())
            print("first response sent")
            COUNT=COUNT+1
        if COUNT > 1:
            try:
                found = re.search('response=(.+?) HTTP', data[0]).group(1)
                found = found.replace("+", " ")
            except Exception as e:
                print(f"error: {e}")
            print(f'{found}')
            response = f'''HTTP/1.1 200 OK\n\n
                        <html>
                        <head></head>
                        <body><p>{found}</p></body>
                        </html>'''
            server_socket.send(response.encode())
            print("response sent")
            server_socket.close()
        else:
            print("test")
        time.sleep(0.01)

def server():
    i=1
    while True:
        c, addr=server_socket.accept()
        child_pid=os.fork()
        if child_pid==0:
                print("\nconnection successful with client " + str(i) + str(addr) + "\n")
                handle_client(c, addr, i)
                break
        else:
                i+=1
                print(f"number: {i}")
        time.sleep(0.01)
        

server()