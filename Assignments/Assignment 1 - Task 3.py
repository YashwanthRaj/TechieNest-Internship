'''
File name - lnbstrindex.py
● Take input from user in string form only and calculate the length of string
● IF length is greater than 7 then display only those character which are
present in even index number
● If length is less than or equals to 7 then display only those character which
are present in odd index number

'''

stringA = input("Enter the string: ")
Strlen = len(stringA)
e=0
o=1
if Strlen > 7:
    print("The Even digits are ")
    while e in range(0,Strlen):
        print(stringA[e])
        e=e+2
else:
    print("The Odd digits are ")
    while o in range(0,Strlen):
        print(stringA[o])
        o=o+2