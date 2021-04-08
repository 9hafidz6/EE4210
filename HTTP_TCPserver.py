import os
import socket
import time
import re

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 4322
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDR,SERVER_PORT))
server_socket.listen(10)

# COUNT = 1

def handle_client(server_socket, addr, i):
    COUNT=1
    while True:
        data=server_socket.recv(1024).decode()
        data = data.splitlines()
        # if not data:
        #     print(f"this is the received data from client {i}: {data}")
        #     print("closing socket")
        #     server_socket.close()
        #     break
        if COUNT == 1:
            if not data[0]:
                continue
            else:
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
            if not data[0]:
                continue
            else:
                found = re.search('response=(.+?) HTTP', data[0]).group(1)
                found = found.replace("+", " ")

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