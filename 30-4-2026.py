# python collection

#list

print("List Examples")

my_list =[10,20,30]
print ("orignal list:",my_list)

# mutability

my_list[0]=100

print("After mutability list:",my_list)

# append()
my_list.append(50)
my_list.append(60)

print("After use build -in function list",my_list)

# max() and min()

print ("Max:", max (my_list))
print ("Min:", min (my_list))

# remove duplicates manually

unique=()

for i in my_list:
    if i not in unique:
        unique.append(i)
print("unique list:".unique)

# tuple

print("tuple examlple")

my_tuple=(1,2,3,4,5)

print("Tuple of:",my_list)

# immutable

#count occurrence

print("count of 2:",my_tple.count(4)))

#swaping using tuple

a,b=10,20
a,b=b,a

print("value",a,b)


