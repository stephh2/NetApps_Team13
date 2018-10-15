"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""
import Debug
import bluetooth

    
def setUpBluetoothClient(port, storage):
    #got bluetooth address from 'Server' typing hciconfig -a in terminal
    serverMACAddress = storage#'B8:27:EB:FB:1B:06'
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    print("[ {} ]  Connecting to {} on port {}".format(Debug.getTimeStamp(), serverMACAddress, port))
    return s

    
def runCommunicationTest(c):
    size = 1024
    while 1:
        text = raw_input() # Note change to the old (Python 2) raw_input
        print "sending: {}".format(text)
        if text == "quit":
            break
        c.send(text)
        data = c.recv(size)
        print "recieved: {}".format(data)
        
    c.close()

##c = setUpBluetoothClient()
##runCommunicationTest(c)