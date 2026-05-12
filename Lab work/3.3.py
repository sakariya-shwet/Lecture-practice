print("lab work 3.3")

print("\nq-->1")
set={1,2,3,4,5}

set.add(6)
set.remove(3)
print(2 in set)
print(set)


print("\nq-->2")

a={1,2,3,4}
b={3,4,5,6}

print("Union",a|b)

print("Intersection:",a|b)

print("defference:",a-b)


print("\nq-->3")

student={"name":"alice","age":20,"grade":"A"}

print("keys",student.keys())

student["city"]="delhi"

student["age"]="21"

del student["grade"]

print(student)


print("\nq-->4")

keys=['id','name','email']
values=[101,'bob','bob@example.com']

for key,value in student.items():

  print(keys ,":", values)

print("\nq-->5")

a="123"
num=int(a)
print(num)

b=[1,2,3]
num2=tuple(b)
print(num2)

c=(4,5,6)
num3=list(c)
print(num3)

pair=[(1,'a'),(2,'b')]
d=dict(pair)
print(d)

a=[11,22,33,44,55]
del a[2]
print(a)






