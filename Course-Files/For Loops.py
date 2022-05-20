# FOR loop runs until the condition becomes false

ab=[45,68,11,5251,615651,651,66,1,16,1,61]
for i in ab:
    print("Hello World")
    print(i)

# Using range function
num = 4
for i in range(0,num):
    print(i) 

# Printing String
aba='Hello wordl'
for i in aba:
    print(i)

# Printing with dictionary
names={"yashwanth":1134,"Sai Nikhil":4568,"Sriram":7413}
for i in names:
    print(i)
for i in names.values():
    print(i)
for i in names:
    print(names[i])

# Printing Pattern
for i in range(1,5):
    for j in range(i):
        print(i,end=' ') 
    print()
    
# Printing stars
for i in range(1,5):
    for j in range(i):
        print('*',end=' ') 
    print()

# Controlling the loop using CONTINUE
for i in 'yashwanth':
    if i == 's' or i == 't':
        continue
    print(i)
    print('Next please')
print('Hello')
print()

# Controlling the loop using BREAK
for i in 'yashwanth':
    if i == 's' or i == 't':
        break
    print(i)
    print('Next please')
print('Hello')
print()

# Controlling the loop using PASS
name='Yashwanth'
for i in name:
    if i == 's' or i =='w':
        pass
    else:
        print(i)

# We can use else with false
for i in range(0,5):
    print(i)
else:
    print('End of the loop')