print("lab work 3.3")

print("q-->1")
set={1,2,3,4,5}

set.add(6)
set.remove(3)
print(2 in set)
print(set)


print("q-->2")

a={1,2,3,4}
b={3,4,5,6}

print("Union",a|b)

print("Intersection:",a|b)

print("defference:",a-b)


print("q-->3")

student={"name":"alice","age":20,"grade":"A"}

print("keys",student.keys())

student["city"]="delhi"

student["age"]="21"

del student["grade"]

print(student)


print("q-->4")

keys=['id','name','email']
values=[101,'bob','bob@example.com']

data = dict(keys ,":", values)

print(data)

