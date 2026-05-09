# LAB WORK 2.2

'''print("q-1-->Maximum number:")

print("\n")

a=int(input("Enter first number:--"))
b=int(input("Enter second number:--"))
c=int(input("Enter third number:--"))


if a>=b and a>=c:
    print("Maximum is ",a)

elif b>=a and b>=c:
    print("Maximum is",b)

else:
     print("Maximum is ",c)


print("q-2-->Minimun number:")

print("\n")


a=int(input("Enter first number:--"))
b=int(input("Enter second number:--"))
c=int(input("Enter third number:--"))


if a<=b and a<=c:
    print("Minimun is ",a)

elif b<=a and b<=c:
    print("Minimun is",b)

else:
     print("Minimun is ",c)



print("q-3-->Maximum number:")

print("\n")

a = int(input("Enter first number:--"))
b = int(input("Enter second number:--"))
c = int(input("Enter third number:--"))
d = int(input("Enter four number:--"))

if a >= b and a >= c and a >= d:
    print("Maximum is", a)

elif b >= a and b >= c and b >= d:
    print("Maximum is", b)

elif c >= a and c >= b and c >= d:
    print("Maximum is", c)

else:
    print("Maximum is", d)


print("q-4-->switch case program:")

print("\n")


a=int(input("Enter first number:--"))
b=int(input("Enter second number:--"))

choice=input("Enter the fnction ===>`+`,`-`,`*`,`/`  ==> ")

if choice=="+":
    print ("addition", a+b)
elif choice=="-":
    print ("substraction", a-b)
elif choice=="*":
    print ("multiplication", a*b)
elif choice=="/":
    print ("division", a/b)

print("q-5 --> Fast food program:")

print("\n<<<Cafe Menu>>>")

print("1.) Pizza")
print("2.) Sandwich")
print("3.) Burger")
print("4.) Pasta")

choice1 = input("Enter your order: ")

match choice1:

    case "1":

        print("\n<<<<Pizza Menu>>>>")
        print("1.) Thin crust Pizza")
        print("2.) Cheese burst Pizza")
        print("3.) Volcano cheese Pizza")

        choice1 = input("Choose pizza type: ")

        if choice1 == "1":
            print("Thanks for ordering Thin Crust Pizza")

        elif choice1 == "2":
            print("Thanks for ordering Cheese Burst Pizza")

        elif choice1 == "3":
            print("Thanks for ordering Volcano Cheese Pizza")

        else:
            print("Invalid pizza choice")

    case "2":

        print("\n<<<<Sandwich Menu>>>>")
        print("1.) Thin crust Sandwich")
        print("2.) Mexican Sandwich")
        print("3.) Potato Onion Sandwich")

        choice2 = input("Choose Sandwich type: ")

        if choice2 == "1":
            print("Thanks for ordering Thin crust Sandwich")

        elif choice2 == "2":
            print("Thanks for ordering Mexican Sandwich")

        elif choice2 == "3":
            print("Thanks for ordering Potato Onion Sandwich")

        else:
            print("Invalid Sandwich choice")

        

    case "3":

        print("\n<<<<Burger Menu>>>>")
        print("1.) Peri Peri Burger")
        print("2.) Cheese Burger")
        print("3.) Schezwan Burger")

        choice3 = input("Choose pizza type: ")

        if choice3 == "1":
            print("Thanks for ordering Peri Peri Burger")

        elif choice3 == "2":
            print("Thanks for ordering Cheese Burger")

        elif choice3 == "3":
            print("Thanks for ordering Schezwan Burger")

        else:
            print("Invalid Burger choice")

    case "4":

        print("\n<<<<Pasta Menu>>>>")
        print("1.) White Sauce Pasta")
        print("2.) Chilli Pasta")
        print("3.) Mexican Pasta")

        choice4 = input("Choose pizza type: ")

        if choice4 == "1":
            print("Thanks for ordering White Sauce Pasta")

        elif choice4 == "2":
            print("Thanks for ordering Chilli Pasta")

        elif choice4 == "3":
            print("Thanks for ordering Mexican Pasta")

        else:
            print("Invalid pizza Pasta")'''

print("q-5-->telecom  program:")

print("\n")

print("i,) press 1 for English")
print("ii,) press 2 for hindi")
print("iii,) press 3 for gujarati")

language=input("Enter your language")

if language=="1":
    print("\nHello good morning how can i help you?")

elif language=="2":
    print("\nNamshkar shubh prabhat mai aapki madad kaise karu?")

elif language=="3":
    print("\nKem cho? hu tamari madad kai reet na kari shaku?")





    
























