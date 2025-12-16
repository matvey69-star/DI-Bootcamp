#Exercise 1
print("Hello world\n" * 4)
#Exercise 2
result=(99*99*99)*8
print(result)
#Exercise 3
>>> 5 < 3 #False
>>> 3 == 3 #True
>>> 3 == "3" #False
>>> "3" > 3 #Error
>>> "Hello" == "hello" #False
#Exercise 4
computer_brand="Apple"
print("I have a " + computer_brand + " computer")
#Exercise 5
name="Matvey"
age=45
shoe_size=42
info="Name: " + name + ", Age: " + str(age) + ", Shoe size: " + str(shoe_size)
print(info)
#Exercise 6
a=4
b=2 
if a>b:
    print("Hello World")
#Exercise 7
user=int(input("Enter your number: "))
if user %2==0:
    print("Your number is even")
else:
    print("Your number is odd") 
#Exercise 8
user=input("Enter your name: ")
if user == "Matvey" or user == "Olga":
    print("Welcome my brother " + user)
else:
    print("Goodbye")
#Exercise 9m
user=int(input("Enter your height in centimeter: "))
if user>145:
    print("You are tall enough to ride roller coaster")
else:
    print("You need to grow more to ride roller coaster")