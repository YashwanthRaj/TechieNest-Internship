# Python comes with many pre built modules for every requirement     

# Time module
import os
import time
print(dir(time))
print()

# But best way to include is
from time import sleep,ctime

print('Hello people!!')
time.sleep(4)
print('Yoy may notice this statement is printed after 4 seconds')
print(time.ctime())

# To delete time module 
del time

# OS mudule and its system command
from os import system

system('date')

del os

# Example with two imports
import subprocess,time
cmd=input("Enter the command: ")
out=subprocess.getstatusoutput(cmd)
if out[0] == 0:
    print('Command found')
else:
    print("Command not found")

# Emoji module 
import emoji

emoji.emojize(":thumbs_up:")