'''#i)

a=input("Enter a number")

int=int(a)
float=float(a)
bool=bool(a)

print("Int:-",int,"type:",type(int))
print("Float:-",float,"type:",type(float))
print("bool:-",bool,"type:",type(bool))

#ii)

a=float(input("Enter a float number:--"))

Int=int(a)

print(f"Float value:{a}")
print(f"int value:{a}")
print("Explanation : int removes decimal part")


#iii)

a=input("Enter true of false:--")
bool=a=="true"

int=int(bool)
str=str(bool)

print("Bool",bool)
print("Int",int)
print("str",str)


#iv)
a=12
b=19.3
c="hello"
d=True
e={1,2,3}
f=(7,8,9)
g={"name":"shwet"}


print(f"Int:{a},type:{type(a)},ID:{id(a)}")
print(f"Float:{a},type:{type(b)},ID:{id(b)}")
print(f"str:{a},type:{type(c)},ID:{id(c)}")
print(f"bool:{a},type:{type(d)},ID:{id(d)}")
print(f"list:{a},type:{type(e)},ID:{id(e)}")
print(f"tuple:{a},type:{type(f)},ID:{id(f)}")
print(f"Dict:{a},type:{type(g)},ID:{id(g)}")'''

#v)

a=10
b=10

print("a=",a,"id:",id(a))
print("b=",b,"id:",id(b))

print("same memory",id(a)==id(b))

b=20

print("a=",a,"id:",id(a))
print("b=",b,"id:",id(b))

print("same memory",id(a)==id(b))


