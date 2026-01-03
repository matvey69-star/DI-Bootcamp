
#Exercise 1: What Are You Learning?
def display_message():
    return "I am learning about functions in Python."

print(display_message())
#Exercise 2: What’s Your Favorite Book
def favorite_book(title):
    return f"One of my favorite books is {title}"
print(favorite_book("Alice in Wonderland"))
#Exercise 3: Some Geography
def describe_city(city, country="Unknown"):
    return f"{city} is in {country}."
print(describe_city("Reykjavik", "Iceland"))
print(describe_city("Paris"))
#Exercise 4: Random Number
import random
def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")
compare_numbers(50)
#Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size="Large", text="I love Python"):
    return f"Shirt size: {size}, Message: '{text}'"
print(make_shirt())
print(make_shirt(size="Medium"))
print(make_shirt("Small",text="Hello!"))
#Exercise 6: Magicians  
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"
make_great(magician_names)
show_magicians(magician_names)
#Exercise 7: Temperature Advice
import random
def get_random_temp():
    return random.randint(-10, 40)
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:  # 32 < temp <= 40
        print("It's really hot! Stay cool.")
main()
#Bonus
def get_random_temp(month):
    if month in [12, 1, 2]:       # Winter
        return random.uniform(-5, 15)
    elif month in [3, 4, 5]:      # Spring
        return random.uniform(10, 25)
    elif month in [6, 7, 8]:      # Summer
        return random.uniform(25, 40)
    else:                         # Fall
        return random.uniform(10, 20)

def main():
    month = int(input("Enter month (1-12): "))
    temp = round(get_random_temp(month), 1)
    
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp <= 23:
        print("Nice weather.")
    elif temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()

