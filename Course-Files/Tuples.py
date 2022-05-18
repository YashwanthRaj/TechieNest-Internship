# Tuples are Datastructure that are similar to Lists . They are ordered and Cannot be changed 

# Homogeneous Tuple will have similar datatype 
t1=(12,35,45,75,121,121)
print(t1)
print(type(t1))

# Heterogeneous Tuple will have different datatypes
t2=(18,63,'Hello',48,'World')
print(t2)
print(type(t2))

# Length of tuple (Number of entries)
print(len(t1))
print(len(t2))

# Checking if the given value exist in given tuple 
print(121 in t1)
print('Yash' in t2)

# Checking the number of entries in the given tuple
print(t1.count(121))
print(t2.count('World'))

# Finding MAximum and Minimum values in given tuple 
# Note that this requires all the values in tuple to be int or float 
print(max(t1))
print(min(t1))

# Slicing concept where we understand positioning of elements in tuple 
a=t1[0]
lastEl = t1[-1]
print(a)
print(lastEl)

# Printing from given range where jump will occure by given number minus 1 
print(t1[0::2])   # here 2-1 is 1 , hence the jump size is  1
print(t1[0::3])   # here jump will be of size 2

# Tuple Inside tuple
t3=(145,'Money',t2)
print(t3)
print(t3[-1])
print(t3[0])

print(t3[-1][2])  # because of tuple inside tuple , we first specify position in t3 , then position in t2