# polymwephism in python
#mean object oriented programmimg is  many forms
# it allows the same method name to perform different task depending on the object or argu used

#1) overloding
#2) overriding

# it also provided bif

# issubclass()
# super()

# 1) method overloding
#mean creating multiple methods with same name but different parameters

class calculator:
     def multiply (self,a,b,c=1):
         return a*b*c

# the object

calc=calculator()
print("multiplication of 2 num",calc.multiply(200,32))
print("multiplication of 3 num",calc.multiply(200,32,45))

# if only 2 arguments passed c takes default values
# if 3 arguments are passed all values are multiplied
# same method name multuply() perform different operations

# 2 method overriding
#mean it occurs when a child class provides a specific implementation of a method already defined in the parent class

class animal:
    def speak(self):
        print("animal makes a sound")

class dog (animal):
    def speak (self):
        print("dog barks")

class cat (animal):
    def speak (self):
        print("cat meow")

# object
a=animal()
d=dog()
c=cat()

a.speak()
d.speak()
c.speak()

# dog and cat inherit from animal
# both child classes override the speak () method

#issubstance()
# mean it used to check weather one class is derived from another class
# syntax: issunstance (child_class ,parent_class)
# it returns values like true,false


class person:
    pass
class student (person):
    pass

print(issubclass(student,person))

# student inherits from function

def add(a,b):
    return a+b

print("addition ",add(100,484))
print("concatenation of str ",add("hello","world"))

# super function
# mean it is used to call method or constructor of the parent class from the child class

class employee:
    def __init__(self,name):
        
        self.name=name
        print("employee constuctor called")

class manager (employee):
    def __init__(self,name,department):

# calling parent  constructor super().__init __(name)

     self.department=department
     print("manager constructor called")

     def display (self):
         print("name",self.name)
         print("department",self.department)

m=manager("shwet","hr")
m.display ()
         




