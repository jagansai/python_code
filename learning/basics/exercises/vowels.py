
# 1.Write a Python program that takes a string input and counts how many vowels (a, e, i, o, u) are in the string.
# Example input: "hello"
# Example output: 2 vowels

def count_vowels(input_string):
    num_of_vowels = 0
    input_string = str(input_string).lower()
    for letter in input_string:
        if letter == 'a' or letter == 'e' \
            or letter == 'i' or letter == 'o' \
            or letter == 'u' :
                num_of_vowels = num_of_vowels + 1

    #  if letter == "a" or letter == "e" or letter =="i" or letter == "o" or letter =="u" or letter =="A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
    #      num_of_vowels = num_of_vowels + 1
    return num_of_vowels
            
input_string = input("Enter a word: ")
num_of_vowels = count_vowels(input_string)
print(f"{num_of_vowels} vowels")