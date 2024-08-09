# collections are nothing but a collection of items.
# for e.g., you can have a collection of numbers
#                        a collection of text
#                        a collection of booleans
#                        a collection of objects ( like Person, Address, etc.)

# In python a collections can be 
# list, set, dictionary 

# Let's look at list. A list in python can simply be wrapped between []
# For e.g., a list of numbers can be represented as [1, 2, 3, 4, 5 ]

numbers = [5, 4, 3, 2, 1]
print(f"Printing numbers: {numbers}")

# To access the individual items in the list, we access by index of the item. 
# in a list, the index starts from 0

print(f"First in the list: {numbers[0]} and the last in the list : {numbers[4]}")

numbers = [0, 1, 2, 3, 4]

print(f"First in the list: {numbers[0]} and the last in the list : {numbers[4]}")

numbers = [3, 4, 1, 2, 5, 0]

print(f"First in the list: {numbers[0]} and the last in the list : {numbers[5]}")

numbers = [1,2,43,4,45,5,5,666,7,8,9,9,10,22,3,55,56,76]
length = len(numbers)
print(f"To calculate the number of items in the list, we can use the method len. So, the number of items in the list numbers is:{length}")

print(f"First in the list: {numbers[0]} and the last in the list : {numbers[length -1]}")

print(f"Third in the list: {numbers[2]}")

# specifically in python, we can get the last element in the list by using -1.

print(f"First in the list: {numbers[0]} and the last in the list : {numbers[-1]}")


# An exercise to identify the minimum of the numbers in the list.
# [1,3,2,4,5] the minimum is 1.
# [ 4, 3, 1, 6, 2] the minimum is 1.
# [ -1, 2, 3, 4, -5 ] the minimus is -5.
def find_minimum(list_of_numbers):
    # Let's assume 100000 is the maximum number.
    minimum_number = 100000
    for number in list_of_numbers:
        if minimum_number > number:
            minimum_number = number
    return minimum_number

numbers = [1,3,2,4,5]
minimum_number = find_minimum(numbers)
print(f"The minimum number in {numbers} is : {minimum_number}")

numbers = [-1, 2, 3, 4, -5 ]
minimum_number = find_minimum(numbers)
print(f"The minimum number in {numbers} is : {minimum_number}")


# numbers = [100001, 100002, 100003  ]
# minimum_number = find_minimum(numbers)
# print(f"The minimum number in {numbers} is : {minimum_number}")


# Exercise is to write a method that accepts list of numbers and returns the maximum of the list.
# [1,2, 4, 5, 3, 0] the maximum is 5.
# [-1, -2, -4, -5, -6 ] the maximum is -1



