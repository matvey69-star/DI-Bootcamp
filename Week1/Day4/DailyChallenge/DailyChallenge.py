#Challenge 1: Multiples of a Number
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)

#Challenge 2: Remove Consecutive Duplicate Letters
word = input("Enter a word: ")
if word == "":
    print("")
else:
    result = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            result += word[i]
    print(result)