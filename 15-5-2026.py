'''# 2D ARRAY WITH LIST
#array inside another array
#store data rows,columms
#it looks like a table or matrix

arr1=[10,11,23,25,81]
arr2=[
    [11,12,13],
    [14,15,16],
    [17,18,19],
]
print(arr1)
print(arr2)

# accessing elements in 2d arr
#syntax arr[rows][columms]

print(arr1[0])
print(arr2[2][1])

# taking input in 2d arr

arr=[]
rows=int(input("Enter rows"))
cols=int(input("Enter cols"))

for i in range(rows):
    row=[]
    for j in range(cols):
         value=int(input(f"arr[{i}][{j}]="))
         row.append(value)
         arr.append(row)
         print(arr)
'''
arr = [
    [1, 2],
    [3, 4]
]
for i in arr:
    for j in i:
        print(j, end=" ")
    print() 


print(" sum of all elements in 2d arr")

arr=[
    [1,2,3],
    [4,5,6],
]
total=0
for i in arr:
    for j in i:
        total +=j
        print("total",total)

# sorting collection datatypes:
#sorting arranging data in order
# types: 1.ascending and decending
# syntax: list.sort()

num=[2,9,3,4,78,6,2,1,5,0,1,7,1,8]
num.sort()
print(num)

num=[2,9,3,4,78,6,2,1,5,0,1,7,1,8]
num.sort(reverse=True)
print(num)

# sorting in str

fruits=["Mango","Apple","Water melon","Banana"]
fruits.sort(reverse=True)
print(fruits)


