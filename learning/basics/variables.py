'''
In any programming language, we hold the data in a variable.
For e.g., 
x = 10 # the value 10 is stored in x.
if you want to change the value of the variable, we can assign some other value to it.
x = 20 
if we want to increment the value by 2.
x = x + 2
if we want to decrement the value by 2.
x = x - 2
if we want, x and y to have the same data, then?

x = y

if we change the value of y to 30 now, will x change??

The answer is `No`.

'''
def print_values(x, y):
    print(f"x={x}, y={y}")

x = 10 
y = x

print_values(x, y)

y = 20

print_values(x, y)


arr = [1000,2000]

print(f"arr={arr}")

x = arr[0]
y = arr[1]

print_values(x, y)

# python way of doing....

x, y = arr[0], arr[1]

print_values(x, y )

x, y = [10, 20]

print_values(x, y )

# we can only unpack as many variables as we have.
# if we have to 2 variables, we can only unpack 2 values from the array.

# we can still unpack by putting a * in front of a variable, like shown below.
x, *y = [1,2,3,4]

print_values(x, y )


# There is another way to completely ignore the rest of the pack.


x, *_ = [1,2,3,4]

print(f"x={x}")


x, *y = input("Enter values seperated by space: ").split(" ")

print_values(x, y )



