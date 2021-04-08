# this is server 1
# TCP server create a web page with 1 text input 
# give to client 
# client input thier own text
import os
import time
import sys
import socket
from _thread import *

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 1234
message = (f"""<html>
            <head></head>
            <body><p>EE-4210: Continuous assessment</p></body>
            </html>""")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_ADDR,SERVER_PORT))

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

def server():
    while True:
        data, addr = server_socket.recvfrom(1024)
        start_new_thread(handle_UDPclient,(server_socket,data,addr))
        print(f"started new thread...")

    server_socket.close()   

#===============================================================================================================================

def main():
    print(f"starting HTTP UDP server...")
    server()
    
if __name__ == "__main__":
    main()