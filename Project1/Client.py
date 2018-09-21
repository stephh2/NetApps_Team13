import socket
import sys

host = '172.29.26.51'
port = 10200
size = 1024

def client():
    print(socket.gethostbyname(socket.gethostname()))
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    #server_address = ('127.0.0.1', 10000)
    server_address = (host, port)
    #sock.bind(server_address)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)


    try:
        
        # Send data
        message = 'This is the message.  It will be repeated.'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()



if __name__ == "__main__"
    client()