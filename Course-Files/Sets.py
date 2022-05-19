# Sets are Data structure which cannot contain any orders among elements hence no indexing , they do not contain list or tuple 
# They do not contain Duplicate elements 

# Declaration type 1
st1 = {41,52,63,88,964,75,151,1151,3135,231651,31}
print(st1)
print(type(st1))

# Declaration type 2
st2 = set([14,54,95,454,'Hello'])
print(st2)
print(type(st2))

# Adding an element
st1.add("Water Bottle")
print(st1)

# Adding multiple elements
st1.update([45,654,654,51])
print(st1)

# Discarding an element
st1.discard('Water Bottle')
print(st1)

st1.remove(964)
print(st1)

# Subrtaction Operation
st3={10,20,30,40,50,60}
st4=set([10,20,30])
print(st3-st4)
print(st3.difference(st4))

# Union Operation
print(st3|st4)

# Intersection
print(st3 & st4)

# Clearing the set
st3.clear()
print(st3)