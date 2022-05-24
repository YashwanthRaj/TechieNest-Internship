# All the networking and communication Applications are possible due to a technique calles Socket Programming 
# Socket Programming by python enables Networking 
# It uses Server client Communication protocols - TCP and UDP

# Server side programming 

import socket
import time

myIp='127.0.0.1'
myPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # iv4 , UDP
    print("Socket object s got cerated..")
    # Binding my IP and Port
    s.bind((myIp,myPort))
    print("Socket got blinded.!")
except:
    print("Please check your socket.!!")

# To recover data sent form client
while 4 > 2: # Infinite while loop
    data=s.recvfrom(100)
    time.sleep(2)
    print(data)

    # Giving a responce to client
    rply=input("Enter your response..")
    rply_new=rply.encode("ascii")
    s.sendto(rply.encode,data[1])
    print("..................")
    
s.close()