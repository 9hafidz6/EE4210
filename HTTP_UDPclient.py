import os
import sys
import time
import socket
import webbrowser

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234


#===============================================================================================================================

def main():
    print(f"starting client...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #send the HTTP GET request to UDP server 
    COMMAND = "GET"
    OBJECT = "/udp.html"
    HTTP_VERSION = "HTTP/1.1"

    # HOST = ""
    # USER_AGENT = ""

    messsage = f"{COMMAND}|{OBJECT}|{HTTP_VERSION}".encode()
    client_socket.sendto(messsage, (SERVER_IP, SERVER_PORT))

    data, addr = client_socket.recvfrom(1024)
    print(f'received from {addr}')
    f = open('udp.html', 'w')
    message = data.decode()
    # message = (f"""<html>
    #                 <head></head>
    #                 <body><p>EE-4210: Continuous assessment</p></body>
    #                 </html>""")
    f.write(message)
    f.close()
    webbrowser.open('udp.html')

if __name__ == '__main__':
    main()