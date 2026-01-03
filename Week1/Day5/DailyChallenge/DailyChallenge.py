#Challenge 1: Letter Index Dictionary
text = input("Enter a word: ")
letter_indices = {}
for i, char in enumerate(text):
    if char.lower() not in letter_indices:
        letter_indices[char.lower()] = []
    letter_indices[char.lower()].append(i)
print(letter_indices)  
#Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
money = int(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= money:
        basket.append(item)
        money -= clean_price
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
#2nd part
items_purchase = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}
wallet = "$100"
money = int(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= money:
        basket.append(item)
        money -= clean_price
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
    #3rd part
    iitems_purchase = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}
wallet = "$1"
money = int(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= money:
        basket.append(item)
        money -= clean_price
if not basket:
    print("Nothing")
else:
    print(sorted(basket))