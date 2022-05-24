'''
File name -  lnbattendance.py
● A Company's CEO wants the attendance of all the employees
● There are e no.of employees and w no.of working days
● Find the maximum number of consecutive days on which all the
employees are present

Example :
Sample Input: 
e= 5 , w= 7
Data = [PPPPP, PPAPP, AAAPP, PAPAP, AAAAA, PAAAP, PPPPP]

Sample output: 
1,7

'''

nu=int(input("Enter the number of employees(Less than or equal to 10): "))

if nu>10:
    print("Your No of employees exceeded my expectations !!")
else:
    e=nu
print()

now=int(input("Enter the number of working days (Less than or equal to 7): "))
if now >7:
    print("There can be only 7 days in a week :) !!")
else:
    w=now
print()

data=[]
i=0
print("Please enter thr value either P or A!!")
while i in range(0,w):
    rec=input("Enter the details of day %s of the week: "%(i+1))
    if len(rec) > e:
        print("Please enter correctly , your data exceeds number of employees!!")
        i=i-1
    else:
        data.append(rec)
    i=i+1
print()
print("The employee attendence details are: ",data)

req='P'*e
j=0
max=[]
while j in range(0,w):
    if data[j]==req:
        max.append(j+1)
    j=j+1

print("The maximum number of consequtive days in which all employees are present : ",max)


