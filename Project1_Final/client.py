import socket
import sys
import argparse
import md5

import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from cryptography.fernet import Fernet
import ClientKeys as keys
import datetime

def getTime() :
    return '['+str(datetime.datetime.now()).split('.')[0].split(' ')[1]+'] '


consumer_key= keys.f.decrypt(keys.encrypted_consumer_key)
consumer_secret=keys.f.decrypt(keys.encrypted_consumer_secret)

access_token=keys.f.decrypt(keys.encrypted_access_token)
access_token_secret=keys.f.decrypt(keys.encrypted_access_token_secret)


def codeTweet(message, k):
    f = Fernet(k)
    mess = f.encrypt(str(message))
    m = md5.new()
    m.update(str(mess))
    m.digest()
    
    print(getTime() + "Encrypt: " + str(k) + " | Ciphertext: " + str(mess))
    j = {  "Key" : k, "Message" : mess, "MD5" : str(m)}
    return json.dumps(j)

def decodeAnswer(j, k):
    d = json.loads(j)
    f = Fernet(k)
    m = md5.new()
    m.update(str(str(d['Message'])))
    m.digest()
    message = f.decrypt(str(d['Message']))
    dic = {"Message" : message, "MD5" : str(m)}
    return dic

class Listener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        tweet = tweet.replace("#ECE4564_Team13", "").strip()
        print(getTime() + "New Tweet : {}".format(tweet))
        
        # Send data
        message = tweet
        k = Fernet.generate_key()
        question_payload = codeTweet(message, k)
        c.sendall(question_payload)
        
        print(getTime() + "Sending data: " + str(question_payload))
        
        coded_data = c.recv(size) 
        decoded = decodeAnswer(coded_data, k)
        answer = decoded["Message"]
        print(getTime() + "Received data: " + str(coded_data))
        print(getTime() + "Decrypt: " + "Using key: " + str(k) + " | Plaintext : {}".format(answer))


        
        return(True)

    def on_error(self, status):
        print(status)





    

def client(port, host, size, t):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    #sock.bind(server_address)
    print(getTime() + 'Connecting to ' + str(host) + ' on port ' + str(port))

    sock.connect(server_address)
    
    return sock;

        



#if __name__ == "__main__":
 
    
# Add required arguments
try:
    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('-brg', help='Add bridge IP')
    parser.add_argument('-p', help='Add bridge port')
    parser.add_argument('-z', help='Add socket size')
    parser.add_argument('-t', help='Add hashtag')

    arg = parser.parse_args()

    if arg.t == None or arg.p == None or arg.brg == None or arg.z == None:
        print('Please set all required input tags. [-t -p -brg -z]')
        sys.exit(1)


    tag = str(arg.t)
    port = int(arg.p)
    host = str(arg.brg)
    size = int(arg.z)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    c = client(port, host, size, tag)
    print(getTime() + 'Listening for Tweets that contain: ' + tag)
    twitterStream = Stream(auth, Listener())
    twitterStream.filter(track=[tag])
    
finally:
    print >>sys.stderr, 'closing socket'
    c.close()
        
