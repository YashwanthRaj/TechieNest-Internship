# Using blocks of code , we can catch and run some blocks of code when error occurs

# Exception Handling using TRY and CATCH function
try:
    n1=int(input('Enter first number: '))
    n2=int(input('Enter the second number: '))
    sum=n1+n2
    print('The sum of those two numbers is: ',sum)
    div=n1/n2
    print('The division value is: ',div)

except ValueError:
    print('Please enter the correct value!!')

except ZeroDivisionError:
    print('The second number entered must be non zero number!!')

# Handling using sys Module/Package
import sys
i=10
try:
    sum=i+'a'
except Exception as e:
    print('Unexpected Error: ',e.__class__())

# try with else
try:
    num=int(input('Enter the number: '))
    assert num%2==0
except:
    print("not an even number!!")
else:
    result=1/num
    print(result)

# Finally exception 
try:
    data=input('Enter data: ')
    print('Hello ',data)
except:
    print('Please check the code once !!!!')
finally:
    print("I am always going to run regardless of your error..")