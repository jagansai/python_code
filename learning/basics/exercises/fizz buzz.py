#2.Write a program that prints the numbers from 1 to 50. 
# But for multiples of 3, print "Fizz" instead of the number, and for the multiples of 5, print "Buzz". 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# Example output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# ...#


def fizz_buzz(up_until):
    print(f"You passed {up_until}")
    start = 1
    while start <= up_until:
        if start % 5 == 0 and start % 3 == 0: 
            print(f"{start}: FizzBuzz")
        elif start % 3 == 0:
            print(f"{start}: Fizz")
        elif start % 5 == 0:
            print(f"{start}: Buzz")
        else:
            print(start)
        start = start + 1

up_until = int(input("Enter the upper_limit:"))
fizz_buzz(up_until)