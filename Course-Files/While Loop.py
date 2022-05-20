# While loops are used when a particular piece of code have to be run forever
# We can include statements like break when condition satisfied

# Declaration TYPE 1
count = 5
while count < 16:
    print('Hello World')
    count=count+1
print()

# Declaration TYPE 2
count1 = 5
while count1 < 16 : count1 = count1+1 ; print('Hello World')

# Operation
l=[12,45,78,23,56,89]
while l:
    print(l.pop())
    print(l)
    print()

# Loop controller
i=0
a='Yashwanth'
while i<len(a):
    if a[i] == 's' or a[i] == 'w':
        i=i+1
        continue  # berak / pass
    print('Current Letter is: ',a[i])
    i+=1