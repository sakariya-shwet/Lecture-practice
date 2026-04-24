# print number from 1 to 10

for i in range(11):
    print(i)

# print  even number

for i in range (1,21):
        if i % 2 == 0:
           print(i)

# sum of first N numbers

n=10
total=0

for i in range (1,n+1):
        total+=i
        print ("sum:",total)

# while loop

n=5
fact=1

while n>0:
    fact*=n
    n-=1
    print("factorial ",fact)

# patteren programs

#right triangle

rows=5

for i in range (1,rows):
    print("*"*i)


# reversed triangle
rows=5

for i in range (rows,0-1):
    print("*"*i)


#nested loops
# multiplication table

for i in range (1,6):
          for i in range (1,11):
           print(i*i,end="")

# break and continue statements

for i in range (1,10):
          if i==5:
           break
print(i)

# reverse a num

num=1234

rev=0

while num>0:
    calc=num%10
    rev=rev*10+calc
    num//=10

print("reversed:",rev)
