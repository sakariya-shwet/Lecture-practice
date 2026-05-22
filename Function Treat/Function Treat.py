print("<<<< Welcome To My Program :-- Function Treat >>>>")

print("\n Welcome To Data Analyzer And Transformer Program")

print("\n Main Menu:")
print("i.) Input Data")
print("ii.) Display Data Summary (built-in function)")
print("iii.) Calculate Factorial (Recursion)")
print("iv.) Filter Data by Threshold (lambda function)")
print("v.) Sort Data")
print("vi.) Display Dataset Statistics")
print("vii.) Exit program")

choice = input("\nEnter your choice: ")

data = ""

if choice == "i":
    data = input("Enter data for a 1D array: ")
    
    print(data)
    print("\nData has been stored successfully!")

elif choice == "ii":

    def Data(text):
     return list(map(int, text))

    user_data = Data(input("Enter data first: "))

    print(user_data)
    print("\nYou've entered in DATA SUMMARY")

    total_elements = len(user_data)
    minimum_value = min(user_data)
    maximum_value = max(user_data)
    sum_of_all_values = sum(user_data)
    average_value = sum_of_all_values / total_elements

    print("total_elements =", total_elements)
    print("minimum_value =", minimum_value)
    print("maximum_value =", maximum_value)
    print("sum of all values  =", sum_of_all_values)
    print("average value =", average_value)

elif choice == "iii":
    num = int(input("Enter a number: "))

    def factorial(n):
        if n < 0:
            return "invalid value"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    result = factorial(num)
    print("factorial is", result)


        
