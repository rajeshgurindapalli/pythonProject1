import datetime
import time
#print(time.time())
print(time.asctime(time.localtime(time.time())))
datetime_object=datetime.datetime.now()
print(datetime_object)
import calendar
s=calendar.prcal(2022)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
print("Select operation.")
print("1.Add")
print("2.Subtract")
while True:
    choice=input("enter choice(1/2):")
    if choice in('1','2'):
        num1=int(input("enter first number:"))
        num2=int(input("enter second number"))
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
