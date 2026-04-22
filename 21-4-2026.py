# python string manipulation

s1='Hello'
s2="World"
s3='''multiline
string'''
s4=r"Raw\n string"

print(s1)
print(s2)
print(s3)
print(s4)

# common string method

s="Hello,world!"

print (s.upper())
print (s.lower())
print (s.split())
print (s.endswith("!"))
print (s.startswith("y"))
print (s.find ("Hello"))
print (s.count ("d"))

#string formatting

name="shwet"
age="15"

#f-string
print (f" Name: {name},Age :{age}")

#.format()
print ("Name : {} ,Age : {} ".format (name,age))

# slicing

s="Hello, python!!"

print(s[0])
print (s[9])
print (s[0:8])
print  (s[:5])
print (s[::-1])

# joinig & splitting in python

words=["python","is","awesome"]
splits="a,b,c"
print(splits.split(","))




