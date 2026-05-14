# ALL TYPE OF PYTHON FUNCTION

# i.) Tnrn
#ii.) Tsrn
#iii.) Tnrs
#iv.)Tsrs

print("\ni). Tnrn")

def greet():
    print("Welcome python students")
greet()

print("\nii). Tsrn")

def add (a,b):
    print(a+b)
add (10,20)

print("\niii). Tnrs")

def message():
    return "Hello python"
print (message())

print("\niv.) Tsrs")

def multiply (x,y):
    return x*y
print (multiply(5,4))

#diagram
# argument ==>   Tnrn
#return   ==>  Tnrs  ,  Tsrn
#both    ==>   Tsrs
# return ends function execution

def calc (a,b):
    return a+b,a-b

x,y=calc(10,5)
print(x)
print(y)


print("\n1d array in python")

print("\nin python a list is used to store multiple values in a single variables")

num=[51,66,44,96,15,35,47]
print(num)

print("\naccessing element using index")

num=[1,2,34,5,]
print(num[0])
print(num[1])

print("\n nagative indexing")

print(num[-1])

print("\n changing list element")

num[1]=20
print(num)

# list traversing using loop")

for i in num:
  print(i)

  #using range () with indexing")
  print("Length of list :",len(num))
  for i in range(len(num)):

      print("Index",i,"value:",num[i])

print("\n add element at end of list")

num.insert(3,30)

print(num)

print("\n remove element")
num=[51,66,44,96,15,35,47]
num.remove(96)

print(num)

print("\n remove at end of list")
num.pop()
num.pop()
print(num)

print("\nsearching in list")

if 2 in num:
    print("Found")


# slicing in list

print(num[1:4])

#sum of list element
num=[51,66,44,96,15,35,47]
total=0

for i in num:
    total +=i
print(total)

total=sum(num)
print(total)







