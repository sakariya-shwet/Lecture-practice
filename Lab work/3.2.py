print("LAB WORK3.2")

print("\nq-->1")

fruits=["apple","banana","orange","grapes","pineapples"]

print("second fruits:--",fruits[1])
print("last fruits:--",fruits[-1])

fruits.append("mango")
print("added mango",fruits)

del fruits[0]
print("after delete first fruit",fruits)

fruits.sort()
print("sort fruits",fruits)

fruits.reverse()
print("Reversed fruits",fruits)


print("\nq-->2")

num=(15,56,85,96,14)

print("Third item",num[2])

#num[1]=100 # <<<<error>>>>


print("\nq-->3")

item=["apple","banana","orange","grapes","pineapples"]
items=("apple","banana","orange","grapes","pineapples")


#item[0]="watermelon"
#print("error tuple is immutable")#<<<<error>>>>

#items[0]="orange"
#print("error tuple is immutable")#<<<<error>>>>

print("\nq-->4")

squares=[i**2 for i in range(1,11)]
print("squares:",squares)
















