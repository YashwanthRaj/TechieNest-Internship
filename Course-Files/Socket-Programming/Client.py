# Client sside programming

import socket
import time

targetIp='127.0.0.1'
targetPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # iv4 , UDP
    print("Socket object s got cerated..")
    # Binding not required here

except:
    print("Please check your socket.!!")

while 3 > 1:
    msg=input("Enter your message: ")
    new_msg=msg.encode("Ascii ")
    s.sendto(new_msg, (targetIp,targetPort))
    print("Data sent !!")
    print("Waiting for response..")
    time.sleep(5)
    print(s.recvfrom(100))