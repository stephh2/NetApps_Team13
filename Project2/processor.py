import RPCServer as MQ
from RPCServer import MQ_data
import BTClient as BT
import Debug

import argparse
import bluetooth



def run(Reciever, Sender, BT_sock, socket_size, ch, method, properties, body):
    print("[ {} ]  Recieved Request Payload : {}".format(Debug.getTimeStamp(), body))
    try:
        text = body
        BT_sock.send(text)
        data = BT_sock.recv(socket_size)
        Sender.basic_publish(exchange=MQ_data['exchange2'], routing_key=MQ_data['key2'], body=data )
        print("[ {} ]  Recieved Answer Payload : {}".format(Debug.getTimeStamp(), data))
    except:
        print "Closing BT connection"
        BT_Sock.close()
        Reciever.queue_delete(queue=MQ_data['queue'])
        Reciever.close()
            
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get parameters from execution.')
    parser.add_argument('-storage', help='Set storage bluetooth Mac Address', required=True)
    parser.add_argument('-p', help='Set storage port number', required=True)
    parser.add_argument('-z', help='Set socket size', required=True)

    # Process args
    args = parser.parse_args()

    # Copy args into vars
    try:
        storage = str(args.storage)
        port = int(args.p)
        socket_size = int(args.z)                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                  
    except Exception as ex:
        print("Missing Information : {} \n Should Have -storage, -p and -z".format(ex))
        sys.exit(1)

    BT_sock = BT.setUpBluetoothClient(port, storage)
    Reciever = MQ.setUpRecieveQ()
    Sender = MQ.setUpSendQ()
    # Consumer orders
    Reciever.basic_consume( lambda ch, method, properties, body:
                              run(Reciever, Sender, BT_sock, socket_size, ch, method, properties, body),
                              queue=MQ_data['queue'], no_ack=True)
    
    print("[ {} ]  Avaiting Client Requests".format(Debug.getTimeStamp()))
    Reciever.start_consuming()


