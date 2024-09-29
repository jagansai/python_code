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



'''
Exercise: 
Read the above lesson on how to get input from the prompt.
Enter a sentence separated by spaces. ( For e.g., Karthik plays good football )

Write different methods by passing the text ( the input that you got) to those methods.

Methods names are
1. break_words - This method should just split the passed in text by spaces. 
2. print_first_word - As the name suggests, this method should print the first word in the sentence 
3. print_last_word - As the name suggests, this method should print the last word in the sentence.
4. print_first_and_last_word - As the name suggests, this method should print the first & last word in the sentence.
'''

