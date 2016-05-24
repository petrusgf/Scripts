#To execute socket you need administrative privileges.
#To connect to socket you need to use telnet ex.:" telnet localhost 1024"
#So you need 2 terminals 
#   1 - Execute python console calling "python "Python Socket and Unittest.py"" or you can run in your IDE
#   2 - Execute telnet "telnet 127.0.0.1 1024" 
# The results will be showed in python console

import socket
import unittest

# Class to test using unittest
class TestStringMethods(unittest.TestCase):
    def test_petrus(self):
        self.assertEquals(data[::-1],data_inv)
        
TCP_IP = '127.0.0.1' # Server IP
TCP_PORT = 1024 # Socket port

#Opening Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connection address:', addr # Printing connection

# listening port
while 1:
    data = conn.recv(1024) # Receiving word
    data_inv = data[::-1] # Inverting word
    if not data: break
    print "received data:", data_inv # Printing inverse word
    unittest.main() # Testing result
conn.close() # Closing connection
