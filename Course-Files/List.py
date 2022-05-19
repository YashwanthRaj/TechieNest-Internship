# List are collection of Mutable and Heterogeneous Data Structure in Python

# Defining Homogeneous List
l1 = [15,32,84,654,999,41,21]
print(l1)
print(type(l1))

# Defining Heterogeneous List
l2 = [36,54,78,'Hello',78,'World']
print(l2)
print(type(l2))

# Creating an empty List
l3 = []
print(l3)
print(type(l3))

# Calculating the length of List
print(len(l1))
print(len(l2))
print(len(l3))

# Adding values at last
print('Before Append ',l2)
l2.append('Hi')
print('After Append ',l2)

# Adding values in a particular index
print("Before adding ",l1)
l1.insert(0,1043)
print('After Adding ',l1)

# Adding multiple values in Last position [TUPLE]
print('Before Adding ',l2)
l2.extend((12,89,69,96))
print('After Adding ',l2)

# Adding multiple values in Last position [LIST]
print('Before Adding ',l1)
l1.extend([12,89,69,96])
print('After Adding ',l1)

# Removing Elements form list BY POSITION
print('Before poping ',l1)
l1.pop() # Default removes last element
print('After poping ',l1)
l1.pop(2)
print('After removing 3rd Element ',l1)

# Removing Elements form list BY VALUE
print('Before removeing 69 ',l1)
l1.remove(69)
print('After removing 69 ',l1)

# Adding two list
l4=l1+l2
print('The added list is: ',l4)

# Indexing 
print(l4[0])

# Slicing
print(l4[1:5])

# Jumping the characters
print(l4[1::2])

# Clearing 
l2.clear()
print(l2)

# Counting Number of times this element occurs
print(l4.count(1043))

# Append 
l2.append(1038)
print(l2)

# Sorting - Arranges elements in Ascending order
print('Before Sorting',l1)
l1.sort()
print('After Sorting',l1)

# Sum of all numbers in given list
print(sum(l1))

# Max and Min
print(max(l1))
print(min(l1))

# Nested Lsit
l5=[12,45,78,36,96,l1]
print(l5)

# Slicing in this Nested list
print(l5[5][1])