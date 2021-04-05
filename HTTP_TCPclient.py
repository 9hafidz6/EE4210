import os
import sys
import time
import socket
import webbrowser

SERVER_IP = '127.0.0.1'
SERVER_PORT = 4321

def main():
    COMMAND = "GET"
    OBJECT = "/tcp.html"
    HTTP_VERSION = "HTTP/1.1"
    CONTENT = ' '

    print(f"starting client...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP,SERVER_PORT))
    print(f'connected to server...')

    message = f"{COMMAND}|{OBJECT}|{HTTP_VERSION}|{CONTENT}".encode()
    client_socket.send(message)
    message = client_socket.recv(1024).decode()
    
    f = open('tcp.html', 'w')
    f.write(message)
    f.close()
    webbrowser.open('tcp.html')

    user_input = input('key in your input here: ')

if __name__ == '__main__':
    main()