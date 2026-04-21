# type conversation

#explicit type conversation

#int() constuctor

#string to int

num_str ="89"

print("type of num_str :",type(num_str))

num_int=int(num_str)

print(f"string`{num_str}`-> int{num_int}, type:{type(num_int)}")

# float to int

num_float=3.89

print(f"float {num_float} -> int: {int(num_float)}")

#boolean to int

print("True ->", int(True))
print("False ->",int(False))

#float to string

str_float_num=3.15

str_float = str(str_float_num)

print(f" (str_float_num) ->str: {str_float} , type:{type(str_float)}")

# string to list/tuple/set

#list

list_1=[1 ,2 ,3 ,4]

print(list_1)

print(type(list_1))

#tuple

tuple_1 =(1 ,2 ,3 ,4)

print(tuple_1)

print(type(tuple_1))

#set

dict_1 ={'a' :1,'b':2}

print(dict_1)

print(type(dict_1))

#id () function- memory address

a=10
b=11
c=12

print(f"{a} : {id(a)}")
print(f"{b} : {id(b)}")
print(f"{c} : {id(c)}")

# with mutable object

list1=[1,2,3]
list2=[1,2,3]
list3=list1

print(f"\n id(list1) : {id(list1)}")
print(f"\n id(list2) : {id(list2)}")
print(f"\n id(list3) : {id(list3)}")
