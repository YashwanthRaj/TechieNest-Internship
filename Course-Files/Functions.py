# Block of code that runs repeatedly 

# Function Declaration 
def myFunction():
    print('You are inside the function')
    return

# Function calling
myFunction()
print()

# Function with Arguements
def display(x,y):
    print('The first number is ',x,' and the second number is ',y)
    return

display(4,6)
print()

# Function with fixed Arguement
def arrange(name,gender='Male'):
    print('The name is: ',name,' and the age is: ',gender)
    return

arrange('Yashwanth')
arrange('Sai Nikhila','Female')
print()

# Call by Reference Example
def callByName(data):
    data.append([1,2,3,4])
    return

data=[12,23,45,86]
print('The old Data is ',data)
callByName(data)
print('The new Data is ',data) 
print()

# Multiple Arguements (We except arguement in the form of tuple)
def myFunction1(*a):
    print(a)
    print(type(a))
    return

myFunction1(45,65,'Hello')
print()

# Accepting arguement in the form of Key Value pair (Dictionary)
def database(**dict):
    print('The name is: ',dict['name'],' and roll number is: ',dict['rollNo'])
    return

myData = {'Yashwanth':'19BLC1043','SaiNikhil':'19BLC1131'}
database(name='Yashwanth',rollNo='19BLC1043')
print()

# Calling teh function and printing the return value
def myData(x):
    return x**x

print(myData(5))
print(myData(7))
print()

def myData1(x,y):
    return x**x,y**2

print(myData1(5,7))
print(myData1(6,8))
print()

### Function Overloading not supported by python , it will take the last defined one
def a():
    print('Hello')

def a():
    print('World')

a()
print()

# Lambda function
var1 = lambda x : x**3
print(var1(5))
print()

# Recursion
def recurFun(x):
    if x>0:
        result = x + recurFun(x-1)
        print(result)
    else:
        result=0
    return result

recurFun(2)