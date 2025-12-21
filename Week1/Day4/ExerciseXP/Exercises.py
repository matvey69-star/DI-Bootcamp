#Exercise 1: Favorite Numbers
# Create a set with my favorite numbers
my_fav_numbers = {3, 7, 21}

# Add two new numbers
my_fav_numbers.add(10)
my_fav_numbers.add(42)

# Remove the last number added
# (since sets are unordered, we explicitly remove the value)
my_fav_numbers.remove(42)

# Create a set with my friend's favorite numbers
friend_fav_numbers = {5, 7, 18}

# Concatenate the two sets using union
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Print results
print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)