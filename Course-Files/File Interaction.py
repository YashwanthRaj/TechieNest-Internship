# Defining a file 

# Creating a file using Write mode 
# In write mode , if a file with same name is alerady present , it wil delete the file and create new one 
file_name = input('Enter file name: ')
fileA=open(file_name,'w')  
fileA.write('Hello Everyone !! , We have successfully cerated the file')
fileA.close()
print()

# File writing from list of content
file_name=input('Enter your file name: ')
names=['Yashwanth is a good boy \n','Rahul is a good boy \n','Musk is a good boy \n']
fileA=open(file_name,'w')
fileA.write('The file is successfully created !! \n')
fileA.writelines(names)

# File Reading the file
fileA=open('names.txt','r')
data=fileA.read()
lineonly=fileA.readline()
fileA.seek(0) 
print(lineonly)
print(data)
fileA.close()
print(type(data))

# moving file in python
import shutil

source='names.txt'
destination='C:/Users/yashw/OneDrive/Desktop/names.txt'
output=shutil.move(source,destination)
print(output)
