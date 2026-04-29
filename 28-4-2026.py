# LIST AND TUPLE IN PYTHON (BASIC & MUTABILITY)

# list -mutable

my_list=[10,20,"shwet"]
print("list:",my_list)
my_list[1]=99
print("list",my_list)
my_list[1]=101
print("list:",my_list)


# tuple -Immutable
#my_tuple=(10,20,30)
#print ("tuplr:",my_tuple)
#my_tuple[0]=40
#string formatting
#indexing and slicing

text="python"

print("first letter:",text[5])
print("second letter:",text[-2])

#slicing

print("first 3 letter:",text[:3])
print("first 2 letter :", text [::3])
students= ["shwet","ved"]
print("first two students :",students [:2])
print("fsecond two students :",students [::2])

# str formatting using list

for student in students:
      print(f"welcome,{student}")
      
