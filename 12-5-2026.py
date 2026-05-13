# remove
num = {1, 2, 3, 4}
num.remove(2)
print(num)  

# discard
num.discard(5)
print(num)

#pop
num.pop()
num.pop()
num.pop()
print(num)


# convert two list into dict use zip()

keys=["name","age","city"]
values=["shwet","15","surat"]

data=dict(zip(keys,values))
print(data)

def greet():
    print("welcome python students!")
greet()


# function with parameter.

def add(a,b):
    print(a+b)

add(1050,2055)


# recursion function

# factorial

def a(n):
    if n==1:
        return 1
    return n* a (n-1)
print(a (5))


# sum of num

def total (n):
    if n ==0:
        return 0
    return n+total (n-1)
print(total (10))


# lambda function

square =lambda x:x*x
print(square(5))

add=lambda a,b :a+b
print(add (10,20))


# list with lambda & map()

num=[1,2,3,4,5,6,7,8,9]
result =list (map(lambda x:x*2,num))

print(result)

# list with lambda &filter

num=[1,2,3,4,56,7,8,]
odd=list(filter (lambda x: x% 2!=0,num))

print(odd)


#Global keywords

x=10001
def show():
    print(x)
show()

count=0
def increment ():
    global count
    count+=1

increment ()
print(count)


# return multiple values
def calc(a, b):
    return a + b, a - b
result = calc(1898, 688)
print(result)

def students():
    name="shwet"
    marks=99.9
    return name , marks
result1 , result2  = students()

print (result1)
print (result2)







