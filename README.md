# EE4210
EE4210 HTTP TCP and UDP servers assignment

files:
1)HTTP_TCPserver.py
    -program which runs TCP server
2)HTTP_UDPserver.py 
    -program which runs UDP server
2)HTTP_UDPclient.py
    -client to send data to UDP server 

How to run:

1)environment setup
    -linux, Ubuntu 20.04
    -python  version 3.85
2)running the program

TCP server:
    -in terminal(in the directory of the files), execute: python3 HTTP_TCPserver.py
    -open browser, type in: 127.0.0.1:4321
    -input text and press enter 
UDP server:
    -in terminal(in the directory of the files), execute: python3 HTTP_UDPserver.py
    -followed by: python3 HTTP_UDPclient.py
        OR
    -create a UDP socket and send string data "GET /udp.html HTTP/1.1" to 127.0.0.1:1234