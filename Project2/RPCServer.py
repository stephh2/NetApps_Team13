"""
SET UP:
sudo rabbitmqctl add_vhost <name>

sudo rabbitmqctl add_user admin password
sudo rabbitmqctl authenticate_user admin password
sudo rabbitmqctl set_permissions -p team13_vhost admin "^admin-.*" ".*" ".*"
sudo rabbitmqctl set_user_tags admin administrator

"""
import Debug
import pika


MQ_data = {
"username": "admin", 
"password": "password",
"vhost": "team13_vhost", 
"exchange": "team13ex",
"exchange2": "team13Rex", 
"queue": "team13Q",
"queue2": "team13R",
"key": "key13",
"key2": "key132"}  

MQ_host = 'localhost'  

def callback(ch, method, properties, body):
    print "RabbitMQ Received : {}".format(body)

def setUpRecieveQ():           
    credentials = pika.PlainCredentials(MQ_data['username'], MQ_data['password'])
    parameters = pika.ConnectionParameters(host=MQ_host,
                                           virtual_host=MQ_data['vhost'],
                                           credentials=credentials)

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=MQ_data['queue'], durable=True)
    channel.exchange_declare(exchange=MQ_data['exchange'], durable=True)
    channel.queue_bind(exchange=MQ_data['exchange'], queue=MQ_data['queue'], routing_key=MQ_data['key'])

    print("[ {} ]  Created  rabbitmq  at  0.0.0.0".format(Debug.getTimeStamp()))

    return channel
    


def setUpSendQ():           
    credentials = pika.PlainCredentials(MQ_data['username'], MQ_data['password'])
    parameters = pika.ConnectionParameters(host=MQ_host,
                                           virtual_host=MQ_data['vhost'],
                                           credentials=credentials)

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    return channel

