# LAB WORK 2.1

print("q-1-->write a python program:")

print("\n")

num=int(input("Enter a number:--"))

if num%2==0:
      print("This is even number")
else:
    print("This is odd number")

print("\n")

print("q-2-->age categorize:")

print("\n")

age=int(input("Enter your age:--"))

if age<=12:
    print("You are child")

elif age<=19:
    print("You are teenager")

elif age<=59:
    print("You are adult")
    
elif age<=60:
    print("You are senior")
    
print("\n")

print("q-3-->the largest number:")

print("\n")

a=int(input("Enter first number:--"))
b=int(input("Enter second number:--"))
c=int(input("Enter third number:--"))


if a>=b and a>=c:
    print("Largest is a",a)

elif b>=a and b>=c:
    print("Largest is a",b)

else:
    print("Largest is a",c)

print("\n")

print("q-4-->check the neutral number:")

print("\n")

number=int(input("Enter a number:--"))

if number >0:
    print("The num is positive")

if number <0:
    print("The number is negative")

else:
    print("The number is neutral")







      
