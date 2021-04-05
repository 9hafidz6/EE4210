import os
import sys
import time
import socket
import webbrowser

SERVER_IP = '127.0.0.1'
SERVER_PORT = 4321

def main():
    print(f"starting client...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((SERVER_IP,SERVER_PORT))
    print(f'connected to server...')

if __name__ == '__main__':
    main()