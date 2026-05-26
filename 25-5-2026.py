# hierachical inheritance
# mean multiple child class inherit from one parent class

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog (Animal):
    def bark(self):
        print("Dog barks")

class Cat (Animal):
    def Meow(self):
        print("Cat Meow")

d=Dog()
c=Cat()

d.eat()
d.bark()
c.eat()
c.Meow()

# hybrid inheritance
# mean is a combianationof multiple and different multilevel inheritance

class a:
    def show (self):
        print("class a")

class b (a):
    def show(self):
        print("class b")

class c (a):
    def show(self):
        print("class c")

class d (b,c):
    def display(self):
        super().show()

obj=d()
obj.display()

# super () follow mro (method resolution order)
# in class d (b,c) python first check class b

#type () function
# the type () function returns the datatype of a variable or object

a=100000
b=85.8
c="python welcome!!"

print(type(a))
print(type(b))
print(type(c))

# dir function
# mean the dir lists all attribute and method of a class or object


class student:
    def __init__(self):          
        self.name = "shwet"      
        
    def show(self):
        print("student name ", self.name)

obj = student()
print(dir(obj))


# isinstance ()
#mean it checks weather an objet belongs to a class

class person:
    pass
obj=person()
print(isinstance (obj,person))

# help ()
# the help display the documentation str of a clas or function

class demo():
    """this is demo class"""

    def show (self):
        """this is method display measge """
help(demo)
