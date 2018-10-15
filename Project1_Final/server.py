import socket
import argparse
import sys
import wolframalpha
import ServerKeys as Keys
from cryptography.fernet import Fernet
import json
import md5
import datetime

def getTime() :
    return '['+str(datetime.datetime.now()).split('.')[0].split(' ')[1]+'] '


#get port
#get backlog size
#get socket size

parser = argparse.ArgumentParser()
parser.add_argument('-p')
parser.add_argument('-b')
parser.add_argument('-z')

args = parser.parse_args()
if args.p == None:
    print('Set server port with -p.')
    sys.exit(1)
if args.b == None:
    print('Set backlog size with -b.')
    sys.exit(1)
if args.z == None:
    print('Set socket size with -z.')
    sys.exit(1)
       
port = int(args.p)
backlog = int(args.b)
size = int(args.z)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server_address = ('localhost', 10100)
server_address = ('', port)

print(getTime() + 'Created socket at 0.0.0.0 on port ' + str(port))

sock.bind(server_address)

# Listen for incoming connections
sock.listen(backlog)

while True:
    # Wait for a connection
    print(getTime() + 'Listening for client connections')

    connection, client_address = sock.accept()
    try:
        print(getTime() + 'Accepted client connection from ' + str(client_address[0])+ ' on port ' + str(port))

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(size)
            print(getTime() + 'Received data: ' + str(data))
            if data:
                
                data1 = json.loads(data)
                
                fz = Fernet(str(data1['Key']))
                input = fz.decrypt(str(data1['Message']))
                hash = data1['MD5']
                
                print(getTime() + 'Decrypt: Key: ' + str(data1['Key']) + ' | Plaintext ' + input)

                
                
                
                #if m != hash:
                 #   break
                
                app_id = Keys.f.decrypt(Keys.encrypted_app_id)
                client = wolframalpha.Client(app_id)
                print(getTime() + 'Sending question to Wolframalpha: ' + input)

                res = client.query(input)
                answer = next(res.results).text
                print(getTime() + 'Received answer from Wolframalpha: ' + answer)
                
                
                mess = fz.encrypt(str(answer))
                print(getTime() + 'Encrypt: Key: ' + str(data1['Key']) + ' | Ciphertext: ' + mess)

                m = md5.new()
                m.update(str(data1['Message']))
                m.digest()
                
                print(getTime() + 'Generated MD5 Checksum: ' + str(m))

                j = {"Message" : mess, "MD5" : str(m)}
                     
                print(getTime() + 'Sending answer ' + mess)

                connection.sendall(json.dumps(j))
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        print('close')
        connection.close()







