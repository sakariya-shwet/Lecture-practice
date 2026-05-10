
print("Welcome to lab work:-- 3.1")

print("\nq-->i.) simple program")

name1 = input("Enter your first name: ")
name2 = input("Enter your last name: ")

print(f"Hello!! {name1} {name2}")


print("\nq->> ii.) vegetable market")

print("\n1.) Apple")
print("2.) Banana")
print("3.) Grapes")

choice = input("Enter your choice: ")

if choice == "1":
    print("The price of Apple is 100₹")

elif choice == "2":
    print("The price of Banana is 50₹")

elif choice == "3":
    print("The price of Grapes is 80₹")

else:
    print("Invalid choice")



print("\nq->> iii.)str program")

s=input("Enter a str")

rev=s[::-1]

print("reversed str",rev)

if s==rev:
    print("Palindrome")
else:
    print("Not palimdrome")



print("\nq->> iv.)upper case and lowercase")

s=input("Enter a str:--")

print("Uppercase:--",s.upper())
print("lowercase:--",s.lower())
print("titlecase:--",s.title())


print("\nq->> v.) find the word (AI) in the sentence")

a="Machine learning and AI are trending"

position = a.find("AI")

print(position)


b=a.replace("AI","Artificial Inteliigence")

print(b)

c="data data mining and big data"

d=c.count("data")

print(d)


print("\nq->> vi.) Split string into a list")

fruits = "apple,banana,grapes".split(",")
print("\nFruit List:", fruits)

print("\nii.)Join list into a sentence")

words = ["Python", "is", "awesome"]
joined_sentence = " ".join(words)
print("Joined Sentence:", joined_sentence)

print("\niii.)Split multiline string into separate lines")
multiline = """Hello
how
are
you"""
print(multiline.split())


print("\nq->> vii.) Check start and end")
text1 = "Hello what are you doing in the  World"


print("Starts with Hello:", text1.startswith("Hello"))
print("Ends with World:", text1.endswith("World"))

word = "Python"
reversed_word = word[::-1]
print("Reversed String:", reversed_word)



















