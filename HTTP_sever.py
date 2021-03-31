# this is server 1
# TCP server create a web page with 1 text input 
# give to client 
# client input thier own text


import os
import sys
import time
import socket
import threading 

SERVER_ADDR = '127.0.0.1'
SERVER_PORT = 8080

def threaded_server():
    

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDR,SERVER_PORT))
    server_socket.listen(10)

    print(f"starting HTTP server...")
    
if __name__ == "__main__":
    main()