#Connect to cs177.seclab.cs.ucsb.edu on port 42293 to interact with your challenge!
import socket
import sys
import configure_pb2
from struct import *
from io import StringIO




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect the socket to the port where the server is listening
server_address = ('cs177.seclab.cs.ucsb.edu', 42293)
sock.connect(server_address)

request = configure_pb2.m0()
request.type = 0
request = request.SerializeToString()
requestlength = (len(request))
requestlength=pack('H', requestlength)
request = request + requestlength

setvalue = configure_pb2.m0()
setvalue.type = 2
setvalue = setvalue.SerializeToString()
setvaluelength = (len(setvalue))
setvaluelength=pack('H', setvaluelength)
setvalue = setvalue + setvaluelength

getvalue = configure_pb2.m3()
getvalue.type = 4
getvalue.flag = "Current value"

error = configure_pb2.m0()
error.type = 5
error = error.SerializeToString()
errorlength = (len(error))
errorlength=pack('H', errorlength)
error = error + errorlength

getvalue = configure_pb2.m2()
getvalue.type = 7
getvalue.count = 0


sock.sendall(request)

while (True):
    data = sock.recv(32)
    print('read')
    command = (data[-1:])
    if (command == b'\x01'): #setvalue
    if (command == b'\x03'): #getvalue
    if (command == b'\x06'): #getcount
    if (command == b'\x08'): #error
    if (command == b'\x09'): #got the flag
        
    





            

