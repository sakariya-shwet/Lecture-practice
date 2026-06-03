print("<<<<print(Welcome! \U0001F44B to python program list>>>>")
'''

print("\n")
print("\U0001F539 Q ==>1")

num=int(input("Enter a random number:=="))
if num >0:
        print("this number is positive num")

print("\n")
print("\U0001F539 Q==>2")


num=int(input("Enter a random number to check even or odd:=="))

if num % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")

print("\n")
print("\U0001F539 Q==>3")

day = int(input("Enter Today number EX.(Sunday=1, Saturday=7)===> "))

if day == 1:
    print("It's Sunday")
elif day == 2:
    print("It's Monday")
elif day == 3:
    print("It's Tuesday")
elif day == 4:
    print("It's Wednesday")
elif day == 5:
    print("It's Thursday")
elif day == 6:
    print("It's Friday")
elif day == 7:
    print("It's Saturday")
else:
    print("Invalid choice! Please enter a number between 1 and 7.")

print("\n")
print("\U0001F539 Q==>4")

age=input("Enter your age :==")

if age>="18":
    if age>="60":
        print("senior citizen age")
    else:
         print("Adult age")
else:
    print(" Minor age")

print("\n")
print("\U0001F539 Q==>5")
while True:
        guess_game=int(input("\nEnter a letter (1-5) (game-guess):=="))

        match guess_game:
                 case 1:
                        print("\n*Wrong gussed \U0001F614 you are so close enter another letter")
                 case 2:
                        print("\n*Wrong gussed \U0001F614 you are so close enter another letter")
                 case 3:
                        print("\n*Yes you guessed right!!")
                        break
                 case 4:
                        print("\n*Wrong gussed \U0001F614 you are so close enter another letter")
                 case 5:
                        print("\n*Wrong gussed \U0001F614 you are so close enter another letter")

print("\n")
print("\U0001F539 Q==6")
a=1
while a<=10:
        print(a)
        a +=1

print("\n")
print("\U0001F539 Q==7")

for i in range(1,15 +1):
        print(i)
        

print("\n")
print("\U0001F539 Q==8")

for i in range(1,11,1):
        print(i)

print("\n")
print("\U0001F539 Q==9")
for i in range(1,11+1):
        if i ==9:
                break
        print(i)

print("\n")
print("\U0001F539 Q== 10")
for i in range(1,11+1):
        if i ==9:
                continue

        print(i)

print("\n")
print("\U0001F539 Q==11")
for i in range(1,11+1):
        if i ==9:
                pass

        print(i)

print("\n")
print("\U0001F539 Q==12")

for i in range(1,4):
        for j in range(1,4):
                print(i,j)

print("\n")
print("\U0001F539 Q==13")

name=input("Enter your name")
hobbie=input("Enter your hobbie")
age=input("Enter your age")
student_id=input("Enter your student_id")

print(f" My name is {name} and my hobbie is {hobbie} ,also age is {age}, my student id {student_id}")

print("\n")
print("\U0001F539 Q==14")


sentence = input("Enter the sentence: ")
print("sentence uppercase:", sentence.upper())
print("sentence uppercase:", sentence.lower())
print("sentence uppercase:", sentence.split())

print("\n")
print("\U0001F539 Q==15")

list=[1,2,3,4,5,6,7,8,9,10]
print(list)
list.append(11)
print(list)

print("\n")
print("\U0001F539 Q==16")

tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple)
print("third element",[3])

print("\n")
print("\U0001F539 Q==17")

animal=["Elephant","Tiger","Lion","Chhetah"]
print("\nAnimal before modified:==",animal)
animal[2]="Goreela"
print(animal)

print("\n")
print("\U0001F539 Q==18")

#animal=("Elephant","Tiger","Lion","Chhetah")
#print("\nAnimal before modified:==",animal)
#animal[2]="Goreela"
#print(animal)

print("Tuple object can't be changed!!!")

print("\n")
print("\U0001F539 Q==19")

num=bool("1 2 3 4 5")
print(num) 

print("\n")
print("\U0001F539 Q==20")

rows=int(input("Enter a row ==>"))
for i in range(1, rows+1):
         print("*" *i)

print("\n")
print("\U0001F539 Q==21")

rows=int(input("Enter a row==>"))
for i in range(1, rows+1):
    print(" " *(rows-i)+"*"*(2*i-1))

print("\n")
print("\U0001F539 Q==22")

rows=int(input("Enter a row ==>"))
for i in range(1, rows+1):
    for j in range(7rows-i):
        print(" " ,end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

print("\n")
print("\U0001F539 Q==23")

num=int(input("Enter a random number to check even or odd:=="))

if num % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")

print("\n")
print("\U0001F539 Q==24")

start=int(input("Enter a random number :=="))
end=int(input("Enter a random number :=="))
total=0

for i in range(start,end+1):
    total +=i

print("sum of all number",total)'''

print("\n")
print("\U0001F539 Q==25")

def a(n):
    if n==1:
        return 1
    return n* a (n-1)
print(a (5))

print("\n")
print("\U0001F539 Q==26")
































                
        


        
        
        















    
