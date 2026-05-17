# write a program to find the lenght of a 1d arry without using built in finction

array=[]
size=int(input("Enter array size==>"))
for i in range (size):
    value=int(input(f"a[{i}]="))
    array.append(value)

count=0
for i in array:
    count+=1

print("length of array",count)
print("orignal array:",array)

# write a program to find a average a 1d array without using built in function

array=[]
size=int(input("enter array size :"))
for i in range (size):
        value=int(input(f"a[{i}]="))
array.append(value)
sum=0
count=0
for i in array:
    sum+=1
    count+=1

average=sum/count
print("Average of array:",average)

print("Q--4")
arr1 = []
arr2 = []
result = []

size = int(input("Enter arr size: "))

print("Enter arr 1 element:")
for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr1.append(value)

print("Enter arr 2 element:")
for i in range(size):
    value = int(input(f"b[{i}] = "))  
    arr2.append(value)

for i in range(size):
    result.append(arr1[i] + arr2[i])

print("array result :", result)

# create arr of num1 / 100
arr=[]
for i in range(1,11):
    arr.append(i)

for i in arr:
    print(i*2)'''

print("Q--5")

arr=[1,2,3,4,5,6,7,8]
num=int(input("Enter num"))
found=False
for i in range (len(arr)):
    if arr[i]==num:
        print(" The num is on Index ",i)
        found=True
        break

if found==False :
    print("not found element ")








         







