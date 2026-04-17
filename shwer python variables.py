#python variables, datatypes and operators.

#variable assignement

x=15
y="Hello world"
z=3.14

# variable naming rules

#must start with  letter and underscore

#cannot start with a number

name20 ="shwet"

print (name20)

#case-sensitive (age,Age and AGE are different variables)

my_var="my world1!!"

_varl=25

print (my_var)
print(_varl)

#data types

#python has several built in datatypes:

#basic types

# numeric types

demo=20 #int
demo1=30.15 #float
complex = "5+j"

#text type

name ="my name is shwet." #string

#boolean type

#bool: ture and false

#type () operator

a=10

print ("type of a :", type(a))

b="hello"

print ("type of b:" ,type(b))

c = True

print ("type of c :",type(c))

#list types data

#list of python

#tuple

#set

#dict

#python operators

'''

1. arithmetic operators
2. assignment operator
3. comparison operator
4. logical operator
5. membership operator
6. identify operator

'''

 # 1. arithmetic operator

a=10
b=3
print ("Addition",a+b)
print ("substraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("modulus",a%b)
print ("exponetiation",a**b)
print ("floor division",a//b)

#assignment operator

x=10
y=2
x+=y

print("+=:",x)#x=x+y
print("-=:",x)#x=x-y
x*=y

print ("*=:",x) #x=x*y
x/=y
print ("/=:",x)
x %=y
print("%=:",y)
print("%=:",x)
y**=x
print("**=:",y) # y=y**x

# comparision operator

x=5
y=8
print("Eual:",x==y)
print("Not Eual:",x!=y)
print("greater than:",x>y)
print("less than:",x<y)
print("greater than or Equal:",x>=y)
print("less than or Equal:",x<=y)
             
#logical operator

a=True             
b=False

print("And:",a and b)
print("Or:",a or b)
print("Not:", not b)
