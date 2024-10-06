# 3.Ask the user for three numbers, and write a program that prints the largest number.
# Example input: 5, 10, 3
# Example output: The largest number is 10

num1 =int( input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int (input("Enter the third number: "))
print = (f"All the numbers in the set are: {num1}, {num2}, {num3}")

if num1 < num3 and num2 < num3:
    print(f"The largest number in the set is: {num3}")
elif num1 < num2 and num3 < num2:
    print(f"The largest number in the set is: {num2}")
else:
    print(f"The largest number in the set is: {num1}")
    

    
    
#[1, 3, 6, 8, 4 3, 9,45,45,99,25,56,85,859,78,98,36,25,54]