'''
File name - lnbtuple.py
● Take input from the user in form of integers (minimum10 & maximum 20
integers)
● Convert the integers into binary tuples
● Use the operators AND & OR for the last two binary tuples and then
display the result
● Now convert the resultant tuple into integer and display the value
'''

elementx = int(input("Enter the first number: "))
elementy = int(input("Enter the second number: "))

x="{0:b}".format(elementx)
y="{0:b}".format(elementy)

'''
x=bin(elementx)[2:]
y=bin(elementy)[2:]
'''

print(type(x),type(y))
x2=[]
y2=[]

for i in range(0,3):
    x2.append(x[i])
    y2.append(y[i])
print(x2,y2)
print()
x3=[]
y3=[]

for i in range(0,3):
    if x2[i] == "1":
        x3.append(True)
    else:
        x3.append(False)

for i in range(0,3):
    if y2[i] == "1":
        y3.append(True)
    else:
        y3.append(False)

print(x3,y3)

addo = []
oro=[]

for i in range(0,3):
    addo.append(x3[i] and y3[i])
    oro.append(x3[i] or y3[i])

print(addo,oro)
print()

addo1=[]
oro1=[]

for i in range(0,3):
    if addo[i] == True:
        addo1.append('1')
    else:
        addo1.append('0')

for i in range(0,3):
    if oro[i] == True:
        oro1.append('1')
    else:
        oro1.append('0')

print(addo1,oro1)

abcd = addo1[0]+addo1[1]+addo1[2]
efgh = oro1[0]+oro1[1]+oro1[2]

print(abcd,efgh)

abcd1 = int(abcd,2)
efgh1 = int(efgh,2)

print(abcd1,efgh1)

