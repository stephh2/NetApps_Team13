import argparse

from cryptography.fernet import Fernet
import socket
import sys
import json

import TextToSpeech as speak
import md5

import datetime

def getMD5(enc_mess):
    m = md5.new()
    m.update(str(enc_mess))
    m.digest
    return str(m)


def getTime() :
    return '['+str(datetime.datetime.now()).split('.')[0].split(' ')[1]+'] '

def codeQuestion(message, k):
    f = Fernet(k)
    mess = f.encrypt(message)
    j = {  "Key" : k, "Message" : mess, "MD5" : getMD5(mess)}
    return json.dumps(j)

def codeAnswer(message, k):
    f = Fernet(k)
    mess = f.encrypt(message)
    j = {"Message" : mess, "MD5" : getMD5(mess)}
    return json.dumps(j)

def decodeIt(j, k):
    d = json.loads(j)
    f = Fernet(k)
    message = f.decrypt(str(d['Message']))
    dic = {"Message" : message, "MD5" : getMD5(str(d['Message']))}
    return dic


def SetUpServer(brg_port,backlog):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('', brg_port)

    print(getTime() + 'Created socket at 0.0.0.0 on port ' + str(brg_port))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(backlog)
    print(getTime() + 'Listening for client connections')
    
    
    
    return sock

    



def SetUpClient( svr_host, svr_port, sock_size ):
    # Create a TCP/IP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (svr_host, svr_port)

    client.connect(server_address)
    print(getTime() + 'Connecting to {} on port {}'.format(svr_host, svr_port))
    
    return client
    
    


def QandA(client, server, size, brg_port):
    
    #from server
    while True:
        # Wait for a connection
        connection, client_address = server.accept()
        try:
            print(getTime() + 'Accepted Connection From {} on port {}'.format(client_address, brg_port))
            while True:
                # GET DATA FROM CLIENT
                data = connection.recv(size)

                if data:
                    print(getTime() + 'Recieved Data from Client : {}'.format(data))
                    
                    d = json.loads(data);
                    k = str(d["Key"])                    
                    
                    decoded = decodeIt(data, k);
                    tweet = decoded["Message"];
                    print(getTime() + 'Decrypt: Key : {} | Plaintext : {}'.format(str(k), tweet))
                  
                    speak.sayIt(tweet)
                    print(getTime()+"Speaking Question : {}".format(tweet))
                    
                    res = codeQuestion(tweet, k)
                    client.sendall(res)
                    print(getTime() + 'Sending Data : {}'.format(res))
                    
                    # Look for the response
                    coded_data = client.recv(sock_size)
                    print(getTime() + "Receiving Data : {}".format((coded_data)))
                    
                    decoded = decodeIt(coded_data, k)
                    answer = decoded["Message"]
                    print(getTime() + "Decrypt : Using Key : {} | Plaintext : {}".format(str(k), answer))
                    speak.sayIt(answer)
                    print(getTime() + "Saying Answer:  {}".format(answer))
                    
                    #SEND DATA TO CLIENT
                    ret = codeAnswer(answer, k)
                    connection.sendall(ret)
                    
                    
                else:
                    print(getTime() + "No More Data From {}".format(client_address))
                    break

                
        
        finally:
            print('closing client')
            client.close()
            print('closing server')
            server.close()



if __name__ == "__main__":

    ap = argparse.ArgumentParser(description='get the arguments')
    
    #GET ARGUEMENTS
    ap.add_argument('-svr-p', help='Add the server port.')
    ap.add_argument('-svr', help='Add the server IP Address.')
    ap.add_argument('-p', help='Add the bridge port.')
    ap.add_argument('-b', help='Add the backlog size.')
    ap.add_argument('-z', help='Add the socket size')

    arg = ap.parse_args()
    
    if arg.svr_p == None or arg.svr == None or arg.p == None or arg.b == None or arg.z == None:
        print('Please set all required input tags. [-srvp -srv -p -b -z]')
        sys.exit(1)

    
    svr_host = str(arg.svr)
    svr_port = int(arg.svr_p)
    brg_port = int(arg.p)
    backlog = int(arg.b)
    sock_size = int(arg.z)
    
    
    server = SetUpServer( brg_port, backlog);
    client = SetUpClient( svr_host, svr_port, sock_size );
    QandA(client, server, sock_size, brg_port)
    
    
