# 3.Ask the user for three numbers, and write a program that prints the largest number.
# Example input: 5, 10, 3
# Example output: The largest number is 10

#temp = input("Enter 3 numbers:" )
#print(temp)
# numbers = 

# num1, num2, num3 = (numbers.split)

# largest = max(num1, num2, num3)

# print(f"The largest number is {largest}")


#numbers = [2,3,4,5,5,6,7,3,54,62,34, 54, 67,89,98,121,78,56,54]

temp = input("Enter numbers separated by comma: ")
temp = temp.replace(" ", "")
numbers = []
for num in temp.split(","):
    numbers.append(int(num))

start = True
max_number = 0
for number in numbers:
    if start == False and number > max_number:
        max_number = number
    elif start == True:
        max_number = number
        start = False

print(max_number)
