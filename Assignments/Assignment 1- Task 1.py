''''
File Name : lnbsum.py
Task : Take User input and process
● Take 5 integer input from the user.
● Remove all numbers less than 9.
● Calculate the sum of remaining numbers

'''
size=int(input("Enter the number of elements: "))

l1=[]
i=0
while i in range(0,size):
    a=int(input("Enter the %sth  Element: "%i))
    l1.append(a)
    i=i+1

print("You have enetered ",len(l1)," Number of elements!")  
print("Original list of elements is : ",l1)

j=0
while j in range (0,len(l1)):
    if l1[j] < 9:
        l1.pop(j)
        j=j-1
    j=j+1

print("After Removing elements below 9: ",l1)
print("The sum of remaining elements are : ",sum(l1))

