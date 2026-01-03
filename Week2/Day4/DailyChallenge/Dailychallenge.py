
# Challenge 1: Sorting

words_input = input("Enter words separated by commas: ").strip()

if not words_input:
    print("No words entered.")
else:
    words_list = words_input.split(",")
    words_list = [word.strip() for word in words_list]  
    words_list.sort()
    sorted_words = ",".join(words_list)
    print("Sorted words:")
    print(sorted_words)

print("\n-----------------------------\n")

# Challenge 2: Longest Word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

# Test examples
print("Longest word tests:")
print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))