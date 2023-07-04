# functions

# write function to return true if even else false
def is_even(num ) :
    if num % 2 == 0 :
        return True
    else :
        return False

def is_odd(num ) :
    return is_even(num) == False


#Let's start with basisc


print( "Hello, world" )
print("Hello, Neeraja")
print("Hello, Jagan")
name = input("Enter name: ")

print(f"Hello, {name}")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print( f"Sum of {num1} + {num2} = {num1 + num2}")


nums = [1,2,3,4,5, 6, 7, 8, 9, 10 ]
names = ["sai", "jagan", "pantula"]

print(f"Printing: {nums}")

for num in nums:
    print(f"{num}")

print("Print numbers in reverse")

for num in nums[::-1]:
    print(f"{num}")

print("Print every alt number in nums")

for index in range(0, len(nums) -2, 4):
    print(f"{index}")

print(f"Only even numbers in the list of {nums=}")

for num in nums:
    if is_even(num) == True:
        print(f"{num}")

print(f"only odd numbers in the list of {nums=}")

for num in nums:
    if is_odd(num):
        print(f"{num}")

# in a list of numbers [1,2,3,4,5,6,7,8,9,10] count the number of evens and number of odds.
# o/p: number of evens: ?
#      number of odds: ?

evens = 0
odds = 0

for num in nums:
    if is_even(num):
        evens += 1
    else:
        odds += 1

print(f"Number of evens:{evens}")
print(f"Number of odds:{odds}")
