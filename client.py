from socket import *
from threading import Thread
  
#setting client
client = socket(AF_INET, SOCK_STREAM)
#connecting client
client.connect(('localhost', 5000))

print('Connected to server sucessfully\nWaiting for other client')

#Function to receive message
def recv():
	#setting/using while loop for receiving message time to time
	while True:
		#receiving message from server of other clients
		msg = client.recv(1024).decode()
		#displaying/printing out the message
		print('\nClient2>' + msg)

#Function to send messges
def send():
	#setting/using while loop for displaying the message again and again
	#So you have unlimited messages limit
	while True:
		#getting mesage
		msg = input('Message>')
		#sending mesage to server
		client.send(msg.encode())

#running 2 Threads of receiving and sending messages
def main():
	print('Client Connected!!\n')
	#creating Thread for receiving and sending message
	recv_msg = Thread(target=recv)
	send_msg = Thread(target=send)

	#starting both the Threads
	recv_msg.start()
	send_msg.start()

#checking if other clients have joined to chat
c = client.recv(1024).decode()
if c == 'Go':
	main()
