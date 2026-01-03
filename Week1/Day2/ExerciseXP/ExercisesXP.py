#Exercise 1: Hello World
print("Hello world\n" * 4)

#Exercise 2: Some Math
result=(99*99*99)*8
print(result)

#Exercise 3: What is the output?
print(15 < 8)        # False
print(5 < 3)         # False
print(3 == 3)        # True
print(3 == "3")      # False
# print("3" > 3)
print("Hello" == "hello")  # False

#Exercise 4: Your computer brand
computer_brand="Apple"
print("I have a " + computer_brand + " computer")

#Exercise 5: Your information
name="Matvey"
age=45
shoe_size=42
info="Name: " + name + ", Age: " + str(age) + ", Shoe size: " + str(shoe_size)
print(info)

#Exercise 6: A & B
a=4
b=2 
if a>b:
    print("Hello World")

#Exercise 7: Odd or Even
user=int(input("Enter your number: "))
if user %2==0:
    print("Your number is even")
else:
    print("Your number is odd") 

#Exercise 8: What’s your name?
user=input("Enter your name: ")
if user == "Matvey" or user == "Olga":
    print("Welcome my brother " + user)
else:
    print("Goodbye")

#Exercise 9: Tall enough to ride a roller coaster
user=int(input("Enter your height in centimeter: "))
if user>145:
    print("You are tall enough to ride roller coaster")
else:
    print("You need to grow more to ride roller coaster")