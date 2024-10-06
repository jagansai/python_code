'''
From an input, take a list of numbers... 

have an array of numbers [1, 3, 4, 3, 5, 6 ]

now get an input from prompt of a number.

to_search = int(input("Enter a number: "))

Now, in the array you need to check how many times the input number occurs.
For e.g., in [1, 3, 4, 3, 5, 6 ] we have 3 occuring 2 times.
Your output should be : 3 appeared 2 times in the array.
'''


numbers = [1,4,4,4,3,5,7,4,7,5,3,8,5]
to_search = int(input("Enter a number: "))
count = 0
for number in numbers:
    if number == to_search:
        count = count + 1
if count == 1:
    print(f"{to_search} appeared {count} time in the array.")
else:
    print(f"{to_search} appeared {count} times in the array.")



