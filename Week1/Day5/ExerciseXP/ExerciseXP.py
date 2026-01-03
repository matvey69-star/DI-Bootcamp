#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result_dict = dict(zip(keys, values))
print(result_dict)

#Exercise 2: Cinemax #2
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} has to pay ${price}")
    total_cost += price
print(f"Total cost for the family: ${total_cost}")
#Bonus
family = {}
total_cost = 0
while True:
    name = input("Enter family member name (or 'quit' to stop): ")
    if name == "quit":
        break
    age = int(input("Enter age: "))
    family[name] = age
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name} has to pay ${price}")
    total_cost += price
print(f"Total cost for the family: ${total_cost}")
#Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara clothes are for {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    brand.pop("creation_date")
    print(brand["international_competitors"][-1])
    print(brand["major_color"]["US"])
    print(len(brand))
    print(brand.keys())
    #Bonus
    more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}
brand.update(more_on_zara)
print(brand)
# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)
disney_users_C = {}
for user in users:
    first_letter = user[0].lower()
    if first_letter not in disney_users_C:
        disney_users_C[first_letter] = []
    disney_users_C[first_letter].append(user)
print(disney_users_C)