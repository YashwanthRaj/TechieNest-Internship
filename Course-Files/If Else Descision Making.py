# These statements decides the direction process
# IF ELSE Statements 

# IF ELSE logic
a=110
if a>10:
    print(a,' is greater than 15')
else:
    print(a,' is not greater than 15')

# NESTED IF ELSE logic
i=110
j=10
if i>j:
    print(i," is gerater than ",j)
    if i > 160:
        print(i,' is greater than 160')
    else:
        print(i,' is not greater than 160')
else:
    print(i," is not gerater than ",j)

# Repetitive IF ELSE
x=10
y=20
if x>y:
    print(x,' is greater than ',y)
elif y>x:
    print(y,' is greater than ',x)
elif x==y:
    print(x,' is equal to ',y)
else:
    print('Value unknown')

# Comparing string values in condition
Myname='Yashwanth'
if Myname=='Yashwanth':
    print('Hello ',Myname)
else:
    print("User not recognized")

# Comparing two conditions AND OR logic
x=20
y=30
z=40
if(x>15) and (y>25):  # TRUE only if both the conditions are satisfied
    print('Both are larger')
else:
    print('Both are not large')

if(x>15) or (y<25):  # TRUE if either of two condition is satisfied
    print('Atleast one is larger')
else:
    print('None of them is larger')


# Using list
userNames = ['Yashwanth','Sai Nikhil','Sriram','Shrinivas']
userName = input('Enter your name: ')
if userName in userNames:
    print("User name present!!")
    print('Hello %s'%userName)
else:
    print('User name not recognized')

# Using Dictionary
UserDatabase = {1043:'Yashwanth',1038:'SaiNikhil',1131:'Shrinivas'}
RegNo = int(input("Enter Reg number: "))
if RegNo in UserDatabase:
    print("User Exist")
    print("Hello %s"%UserDatabase[RegNo])
else:
    print('User name not recognized')

# Dictionary another example
DataPasd = {'Yashwanth':4561,'Shrinivas':1234,'SaiNikhil':7894,'Sriram':4568}
user = input("Enter the user name: ")
if user in DataPasd:
    print("Welcome !! ")
    psd = int(input("Enter the password : "))
    if psd == DataPasd[user]:
        print("Yes your password is correct!!")
    else:
        print('You are an imposter !!')
else:
    print('You are not present ')
