import os
import sys
import socket
from _thread import *
import threading
import webbrowser
import time 
import re

SERVER_ADDR = '127.0.0.1'
UDP_SERVER_PORT = 1234
TCP_SERVER_PORT = 4321

#===============================================================================================================================

def handle_UDPclient(udp_socket,data, addr):
    #process the HTTP GET request here 
    COMMAND, OBJECT, HTTP_VERSION = str(data.decode()).split('|')
    print(f'udp server received: {COMMAND} {OBJECT} {HTTP_VERSION} from {addr}')
    if COMMAND == "GET" and OBJECT == "/udp.html" and HTTP_VERSION == "HTTP/1.1":
        message = (f"""<html>
                    <head></head>
                    <body><p>EE-4210: Continuous assessment</p></body>
                    </html>""")
    else:
        message = (f"""<html>
                    <head></head>
                    <body><p>Invalid Command</p></body>
                    </html>""")
        # message = 'HTTP/1.1 200 OK\n\nHello world'
    udp_socket.sendto(message.encode(),addr)
    sys.exit()

#===============================================================================================================================

def UDP_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((SERVER_ADDR,UDP_SERVER_PORT))
    while True:
        data, addr = udp_socket.recvfrom(1024)
        start_new_thread(handle_UDPclient,(udp_socket,data,addr))
        print(f"new UDP connection...")
    udp_socket.close()   
#===============================================================================================================================
#==                                                                                                                           ==
#==                                                                                                                           ==
#==                                                                                                                           ==
#===============================================================================================================================

def handle_TCPclient(Client,address):
    print(f"handling TCP client...")
    request = Client.recv(1024).decode()
    request = request.splitlines()
    #print(f'{request[0]}')
    #will get 3 headers from the first line 
    COMMAND, OBJECT, HTTP_VERSION = str(request[0]).split(' ')
    print(f"the 3 received are: {COMMAND} {OBJECT} {HTTP_VERSION}")

    # Send HTTP response
    if COMMAND == "GET" and HTTP_VERSION == "HTTP/1.1":
        response = '''HTTP/1.1 200 OK\n\n
                        <html>
                        <form action="/127.0.0.1:4321" method="GET">
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
        Client.sendall(response.encode())
        # Client.send(response.encode())
    else:
        print("something wrong here...")

    request = Client.recv(1024).decode()
    request = request.splitlines()
    print(f'second response: {request[0]}')
    # print(f"second response: {request}")
    # request = "GET /my-handling-form-page?response=test HTTP/1.1"

    found = re.search('response=(.+?) HTTP', request[0]).group(1)
    print(f'{found}')
    response = f'''HTTP/1.1 200 OK\n\n
        <html>
        <head></head>
        <body><p>{found}</p></body>
        </html>'''
    Client.send(response.encode())
    print("response sent")

    Client.close()

#===============================================================================================================================

def TCP_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((SERVER_ADDR,TCP_SERVER_PORT))
    tcp_socket.listen(10)
    
    # while True:
    #     Client, address = tcp_socket.accept()
    #     print(f"connected to {address[0]} and {address[1]}")
    #     start_new_thread(handle_TCPclient,(Client,address))
    #     print(f'new TCP connection')
    Client, address = tcp_socket.accept()
    print(f"connected to {address[0]} and {address[1]}")
    handle_TCPclient(Client, address)
    
    tcp_socket.close()

#===============================================================================================================================

def main():
    print(f"starting HTTP UDP server...")
    t1 = threading.Thread(target=UDP_server,args=())
    print(f"starting HTTP TCP server...")
    t2 = threading.Thread(target=TCP_server,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'program ended')

if __name__ == "__main__":
    main()