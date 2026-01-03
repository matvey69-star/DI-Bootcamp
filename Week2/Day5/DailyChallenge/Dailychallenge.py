#DaylyChallenge: Old MacDonald’s Farm
# Step 1–4: Create the Farm class
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"

        info += "\n    E-I-E-I-0!"
        return info


# Step 5: Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

#Bonus Expand the Farm
def get_animal_types(self):
        return sorted(self.animals.keys())
        def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_list = []

        for animal in animal_types:
            if self.animals[animal] > 1:
                animals_list.append(animal + "s")
            else:
                animals_list.append(animal)

        animals_str = ", ".join(animals_list[:-1])
        animals_str += " and " + animals_list[-1]

        return f"{self.name}'s farm has {animals_str}."
        def add_animal(self, **animals):
        for animal, count in animals.items():
            if animal in self.animals:
                self.animals[animal] += count
            else:
                self.animals[animal] = count
