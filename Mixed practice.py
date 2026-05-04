#Bill generator (price + tax)

Price=int(input("Enter your bill amount:-"))
tax=int(input("Enter the tax % :-"))

Bill=Price+(Price*tax)/100
print("your total bill is",Bill)
