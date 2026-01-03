#Exercise 1: Cats
# Step 0: Define the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Shadow", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1

    if cat2.age > oldest_cat.age:
        oldest_cat = cat2

    if cat3.age > oldest_cat.age:
        oldest_cat = cat3

    return oldest_cat

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

# Exercise 2: Dogs
# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2: Create Dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)

# Step 3: Print dog details and call methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")

#Exercise 3 : Who’s the song producer?
# Step 1: Create the Song class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Create a Song object
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
# Call the method
stairway.sing_me_a_song()

# Exercise 4: Afternoon at the Zoo
# Step 1: Define the Zoo class
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}:")
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()

            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []

            self.grouped_animals[first_letter].append(animal)

    def get_groups(self):
        for letter, animals in self.grouped_animals.items():
            print(f"{letter}: {animals}")

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()