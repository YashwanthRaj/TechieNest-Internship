'''
File name : lnbcal.py
● Take 2 integer input from user and print their products(their multiplication)
● IF product is greater than 500 then return their sum
● If the product is smaller than 500 then return "Hello LNB code is running
fine !!"


'''

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=a*b

if c > 500:
    print("The multiplied value is: ",c)
else:
    print("The value is not greater than 500 , but the code is running fine :)")