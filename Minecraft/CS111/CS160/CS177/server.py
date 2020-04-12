#Connect to cs177.seclab.cs.ucsb.edu on port 42293 to interact with your challenge!
import socket
import sys
import configure_pb2
from struct import *




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

a = configure_pb2.m1()
a.type = 0
a.body = "hello!"
# Connect the socket to the port where the server is listening
server_address = ('cs177.seclab.cs.ucsb.edu', 42293)
sock.connect(server_address)
s = a.SerializeToString()
length = len(s)
message=pack('H', length)
sock.sendall(message)
sock.sendall(s)
print(message)
print(s)
while (True):
    data = sock.recv(32)
    print(data)
    print('fixed')



            

