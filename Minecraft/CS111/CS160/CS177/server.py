#Connect to cs177.seclab.cs.ucsb.edu on port 42293 to interact with your challenge!
import socket
import sys

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
# Main Function 
mydict = my_dictionary() 


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# Connect the socket to the port where the server is listening
server_address = ('cs177.seclab.cs.ucsb.edu', 42293)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
print("went ok")
length = False
strlen = 0
counter = 0 
type = 0
flag = ""
while (True):
    if (length == False):
        strlen = sock.recv(4)
        length = True
    else:
        data = proto
        while (counter < strlen):
            moredata = sock.recv(strlen)
            data = data + moredata
            counter = counter + len(moredata)
        parse(data)
        type = data.type
        if (type == 1):
            key = data.body.key
            message = data.body.new
            mydict.add(key,message)
        if (type == 3):
        if (type == 6):
        if (type == 8):
        if (type == 9):
            flag = data[1]
print(flag)

            

