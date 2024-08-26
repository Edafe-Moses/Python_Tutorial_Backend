import socket
import sys
import time

#end of imports ###
### inint ###
s = socket.socket()
host = socket.gethostname()
print('server will start on host : ', host)
port = 8800
s.bind((host,port))
print("")
print(" server done binding tohost and port successfully")
print("")
print(" server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()

print(addr, " Has connected to the server and is now online ")
print("")

while 1:
    message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    print("message has been sent...")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(" client : ", incoming_message)
    print("")