# Exercise 1: Pets
# ----- Given Classes -----
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# ----- Step 1: Create the Siamese class -----

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# ----- Step 2: Create a list of cat instances -----

bengal_cat = Bengal("Leo", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Luna", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]


# ----- Step 3: Create a Pets instance -----

sara_pets = Pets(all_cats)


# ----- Step 4: Take cats for a walk -----

sara_pets.walk()

# Exercise 2: Dogs
# ----- Step 1: Create the Dog class -----

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight"
        else:
            return "It's a tie!"


# ----- Step 2: Create Dog instances -----

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 22)


# ----- Step 3: Test dog methods -----

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))

#Exercise 3: Dogs Domesticated
import random
from dog import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]
        for dog in args:
            dog_names.append(dog.name)
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
dog1 = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 15)
dog3 = PetDog("Max", 4, 20)
dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()
dog1.do_a_trick()

#Exercise 4: Family and Person Classes
# ----- Step 1: Create the Person class -----

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


# ----- Step 2: Create the Family class -----

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(
                        f"You are over 18, your parents Jane and John accept "
                        f"that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")


# ----- Tests -----

my_family = Family("Smith")

my_family.born("Alice", 17)
my_family.born("Bob", 20)
my_family.born("Charlie", 12)

print("\n--- Check majority ---")
my_family.check_majority("Alice")
my_family.check_majority("Bob")

print("\n--- Family presentation ---")
my_family.family_presentation()