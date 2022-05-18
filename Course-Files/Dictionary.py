# Dictionary is a key Value pair Data Structure in python which is Changable and no Duplicate values are allowed

# Null value declaration 
d1={}
print(d1) 

# Value inside Dictionary 
d2={'name':'Yashwanth','College':'VIT','DOB':'27/05/2002'}
print(d2)
print('The name is :',d2['name'])

# To add and element
d1['name']='Rahul'
d2['Age']=20
print(d1)
print(d2)

# To delete an element 
del d1['name']
del d2['College']
print(d1)
print(d2)

# To delete and Entire dictionary
d2.clear()
print(d2)

# Adding Dictionary inside Dictionary 
d3={'name':'Yashwanth','College':'VIT','DOB':'27/05/2002'}
d4={'Company':'TechieNest','Programme':'Python'}
d3['Internship']=d4
print(d3)