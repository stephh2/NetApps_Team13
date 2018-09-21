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

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #server_address = ('localhost', 10100)
    server_address = ('', 10200)

    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >>sys.stderr, 'no more data from', client_address
                    break
                
        finally:
            # Clean up the connection
            print('close')
            connection.close()


if __name__ == "__main__"
    server()