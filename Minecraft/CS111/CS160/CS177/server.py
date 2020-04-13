#Connect to cs177.seclab.cs.ucsb.edu on port 42293 to interact with your challenge!
import socket
import sys
import configure_pb2
from struct import *
from io import StringIO




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dictionary = dict()


# Connect the socket to the port where the server is listening
server_address = ('cs177.seclab.cs.ucsb.edu', 42293)
sock.connect(server_address)

request = configure_pb2.m0()
request.type = 0
request = request.SerializeToString()
requestlength = (len(request))
requestlength=requestlength.to_bytes(2, 'big')
request = requestlength + request

setvalue = configure_pb2.m0()
setvalue.type = 2
setvalue = setvalue.SerializeToString()
setvaluelength = (len(setvalue))
setvaluelength=setvaluelength.to_bytes(2, 'big')
setvalue = setvaluelength + setvalue

getvalue = configure_pb2.m3()
getvalue.type = 4
getvalue.flag = "Current value"


getvalue = configure_pb2.m2()
getvalue.type = 7
getvalue.count = 0






while (True):
    sock.sendall(request)
    data = sock.recv(32)
    m_len = data[0:1]
    length = len(m_len) + 2
    while (len(data) < length):
        data = data + sock.recv(32) 
    #by now, should have gotten the whole package
    print('server response is')
    print(data)
    command = (data[3:4])
    print('command is')
    print(command)
    if (command == b'\x01'): #setvalue
        print('f1')
        temp = configure_pb2.m1()
        temp.ParseFromString(data)
        break
    if (command == b'\x03'): #getvalue
        print('f2')
        temp = configure_pb2.m2()
        temp.ParseFromString(data)
        break
    if (command == b'\x06'): #getcount
        getvaluemessage = getvalue.SerializeToString()
        getvaluelength = (len(getvaluemessage))
        getvaluelength=getvaluelength.to_bytes(2, 'big')
        getvaluemessage = getvaluelength + getvaluemessage
        print(getvaluemessage)
        sock.sendall(getvaluemessage)
        print('sent')
    if (command == b'\x08'): #error
        print('error')
        print(data)
        break
    if (command == b'\x09'): #got the flag
        print('program finished')
        break


        
    





            

