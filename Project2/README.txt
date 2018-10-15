SYSTEM SYNTAX:
to run storage.py:
	python storage.py -p <port> -b <backlog size> -z <size>
	- port : the bluetooth connection port
	- backlog size : the size of the backlog
	- size : the data size of information transfered between the processor and storage

to run processor.py:
	python processor.py -p <port> -storage <bluetooth address> -z <size>
	- port : the bluetooth connection port
	- bluetooth address : the address of the bluetooth connection
	- size : the size of the  bluetooth socket connection

to run client.py:
	The client can do one of six commands:
	- ADD : Add book info into storage.
		python client.py -proc <Processor IP Addr> -action ADD -book <Book Info>
	- BUY : Buy more books.
		python client.py -proc <Processor IP Addr> -action BUY -book <Book Info> -count <Bought Count>
	- SELL	: Sell books.
		python client.py -proc <Processor IP Addr> -action SELL -book <Book Info> -count <Sell Count>
	- DELETE : Delete book info from storage
		python client.py -proc <Processor IP Addr> -action DELETE -book <Book Info>
	- COUNT	: Get specific book’s count in stock
		python client.py -proc <Processor IP Addr> -action COUNT -book <Book Info>
	- LIST	: List all book info inside storage
		python client.py -proc <Processor IP Addr> -action LIST





LIBRARIES:
	socket
	datetime
	argparse
	sys
	pymongo
	thread
	time
	Queue
	bluetooth
	json
	os
	subprocess
	RPi.GPIO
	math
	pika

CONTRIBUTIONS:

	Logan:
		Serialize payload by JSON
		Use correct MongoDB element data format
		Encapsulated LED/MongoDB functions into an individual class LED.py/MongoDB.py
		Print checkpoints wirh corrct format and required info
		Add new item to mongodb
		Detele item from mongodb
		Increase/Decrease item stock number
		List out all database items
		Get item stock number
		Use RGB LED to display how many kind of books’ information in database
		LED display can running with MongDB simultaneously (Multi-thread needed)
		
	Sawyer:
		Serialize payload by JSON
		Print checkpoints wirh corrct format and required info
		Client can send request payload and get answer payload to processor via RabbitMQ
		Moral Support
		Wired Up LED Supervision

	Stephanie:
		All Bluetooth Mac addr/ip addr are not hard coded into the code
		Print checkpoints wirh corrct format and required info
		Client can send request payload and get answer payload to processor via RabbitMQ
		Processor can send request and get answer payload to storage via Bluetooth socket connection
		Turn off all LEDs after program is terminated
		Tyed the README.txt

