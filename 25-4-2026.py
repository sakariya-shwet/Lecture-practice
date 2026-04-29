# type conversion

#Implicit type

# Explict type

# implicit: python does it automatically,

# explicit: you tell python exactly what to convert to using built in fuctions.

# convert to int()

type1="42"

print(int(type1))
print(type(type1))

a=10
b=10.20

print("type a", type(a))
print("type b", type(b))

c=a+b

print ("type c",type(c))

print(c)

# demo

x="10"
y="20"
z=x+y
print(z)

# bool(): convert to bool value

print(bool(1))
print(bool(0))
print (int(True))
print(int(False))
print(bool("Hello"))
print(bool(None))

# str(): convert to str
print (type(str(100)))
print(str(3.1459))

# sequence conversion :list(),tuple(),set()

text="hello"
print(list(text))
print(tuple(text))
print(set(text))

# safe conversion pattern

user_input =input("Enter a number:")

try:
    number=float (user_input)
    print(f"converted:(number)*2=(number*2)")
except value :
        print("Invalid input,please choose numeric value")


