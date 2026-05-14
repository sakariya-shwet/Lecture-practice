print("Welcome lab work 4.1")
print("\nq-->1")

num = [15, 62, 47, 96, 25, 44]

print(num)

print("LENGTH", len(num))
print("MAX", max(num))
print("MIN", min(num))
print("SORT", sorted(num))
print("TYPE", type(num))


print("\nq-->2")

def Factorial(n):
    if n<0:
        return "invalid value"
    elif n==0 or n==1:
        return 1
    else:
        return n* Factorial (n-1)

print( Factorial (7))
print( Factorial (10))

print("\nq-->3")


def square_list(num):
    return [i**2  for i in num]
    num=[12,3,4,5]
print(square_list(num))







