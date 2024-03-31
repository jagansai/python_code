'''
 - numbers
    - integers : -1 ....0, 1 , 2, 3, ...
    - decimals : -1.2 , 0, 1.1, 2.2
    - fractions : 0.5, 0.6
    
 - text : "This is a text". "ABC" . This can be represented in python with double or single quotes
 - boolean : True or False.
'''


''''
A data is contained in a variable. The variable names cannot be seperated by a space.
For e.g., 
Below are valid variable names
num
nums
num2
num_of_evens

Below are invalid variable names
-num
num of evens 
'''


'''
In python, we don't need to specify the type of the data.
For e.g., you don't need to specify if the data is number or text or boolean
'''

a = 10

print( "Printing the data in the variable 'a' having number:" , a)

a = "This is a text"

print("Printing the data in the variable 'a' having text: ", a)

a = True

print("Printing the data in the variable 'a' having text: ", a)




num = 10
# increment num by 10.

num = num + 10

print(f"The value of num is {num}")


# decrement num by 5

num = num - 5
print(f"The value of num is {num}")

# multiply num by 5

num = num * 5
print(f"The value of num is {num}")

# divide num by 5
num = num / 5
print(f"The value of num is {num}")


# some operations on text.

text = "this is a text"

print(f"Printing the contents of text: {text}")

text2 = text.upper()

print(f"Printing the contents of text: {text2}")

text2 = text.capitalize()

print(f"Printing the contents of text: {text2}")

'''
Below code, is to demonstrate the utility text functions in python.
'''
# printing first character in "this is a text"
character = text[0]
print(f"First character in {text}: {character}")

character = text[1]
print(f"Second character in {text}: {character}")
# in a text of length 5, what is the index of last character? 4
# in a text of length 10, what is the index of last character? 9

length = len(text)

print(f"The length of {text} : {length}")

last_character = text[len(text) -1]

print(f"The last character of '{text}' is {last_character}")


# python specific.
last_character = text[-1]
print(f"The last character of '{text}' is {last_character}")

# substring of a text. Get the text between 1st and 3rd character.
substring_text = text[0:3]
print(f"Text between 1st and 3rd character: {substring_text}")


substring_text = text[1 : 4]
print(f"Text between 2nd, 3rd and 4th character: {substring_text}")

substring_text = text[1:]

print(f"Text between 2nd to the end of the string of the string: {substring_text}")

text1 = "T"
text2 = "his"
text3 = text1 + text2
print(f"Joining {text1} and {text2} : {text3}")

for line in open("learning\\basics\\file.txt"):
    #print(line)  
    line = line[0].capitalize()+ line[1:]
    print(line)