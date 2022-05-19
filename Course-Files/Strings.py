# Strings are collection of heterogeneous characters

# Declaration
st1='Hello World'
st2="My name is Yashwanth"

# Length
print(len(st1))

# Concatination 
st3=st2+" "+st1
print(st3)

# Printing Multiple times
print(st1*5)

# Formating / Adding variable in print statement
st4="Adam's"
st5="Apple"
print('Hey %s'%st4)
print('Hello {} and {}'.format(st4,st5))

# Split
print(st1.split())
print(st2.split('a'))

# Indexing
print(st1[1],st2[5])
print(st1[0:5])
print(st3[::3])

# Searching 
print('y' in st2)
print('Yash' in st2)
print('yoda' in st2)

# Finding the location
print(st1.find('Hello'))
print(st1.find('World'))
print(st1.find('l'))

# Find the location in a given substring
print(st1.find('l',0,6))