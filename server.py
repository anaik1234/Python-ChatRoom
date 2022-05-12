from socket import *
from threading import Thread

#Setting up the Server
server = socket(AF_INET, SOCK_STREAM)
#Binding with specific address
server.bind(("localhost", 5000))
#listening on the server
server.listen(2)

print('Server Started')

#all clients list
conns = []

#creating main function
def chat(conn1):
	'''Setting while loop for receiving msgs from client and sending it to other
	client'''
	while True:
		#receiving msg
		msg = conn1.recv(1024).decode()

		'''setting while loop for sending every client except the client from
		the data received for display the message'''
		for x in conns:
			#checking client
			if x != conn1:
				#sending data
				x.send(msg.encode())

while True:
	#accepting client
	client, addr = server.accept()
	print('Client Connected')

	#appending client for later chatting use and few other functions
	conns.append(client)

	#activating client
	#checking number of clients
	client_number = len(conns)
	'''if clients are 2, that could mean there was a client waiting and a other
	client joined so both the client1 and the client2 should activate.
	As there are only 2 clients on the server, the server will set a for
	loop to tell the both clients that there is other client to talk with and
	the clients will get activated'''
	if client_number == 2:
		for x in conns:
			x.send('Go'.encode())

	'''if there more than 2 clients than server will authomaticallly activate
	the new client because there are clients already joined to talk with'''
	elif client_number > 2:
		client.send('Go'.encode())

	#Creating a thread for client for chatting
	client_chat = Thread(target=chat, args=[client])
	#starting the thread
	client_chat.start()
