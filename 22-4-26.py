# PYTHON STATEMENTS

#if statement

dooropen =False

if dooropen:
    print ("Welcome to home:")
else:
    print("Meet me again tommorow:")

# if... elif.else.statements

# check positive,negative,zero

num=int(input("Enter a number"))

if num>0:
        print(f"{num}positive number")
elif num<0:
       print(f"{num}negative")
else:
       print("Zero")

# find largest of  two numbers

a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print ("Largest is ",a)
else:
    print("Largest is",b)

# check leap year

year=int(input("Enter year"))

if(year % 4==0 and year% 100!=0) or (year % 100 ==0):
    print("Leap year")

else:
    print("Not  a leap year")

# loop in python


# i] while loop

i=1
while i<6:
    print(i)
    it=1

    
# ii] for loop

for i in range(5):
    print(i)
