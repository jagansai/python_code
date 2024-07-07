'''
If we want to repeat a work, then the approach is to wrap the work in a function / method 
and just call the method.
The syntax for writing a method is

def <function_name>():
    # the implementation of the method.

'''

# Let's consider an example below.

def print_hello():
    print("Hello")
    

print_hello()

# methods also take arguments. That is one can pass a value to a method and use that value in the method.

def print_hello(times):
    start = 1
    while start <= times:
        print(f"{start}: Hello")
        start = start + 1
        

print_hello(5)
print_hello(1000)


# Taking the earlier example in the loops, we can wrap the whole implementation of looping until 
# in a method and repeatedly call the method.


def loop_until( upper_limit, loop_until_value ):
    if upper_limit < loop_until_value:
        loop_until_value = upper_limit
        
    print(f"Upper limit:{upper_limit}\nWe are looping until:{loop_until_value}")
    start = 1

    while start <= loop_until_value:
        print("Hello!")       
        start = start + 1


loop_until( 5, 3 )
loop_until( 6, 3)
loop_until(5, 10 )
loop_until( -1, 10 )


# write a method, that does not take any argument. Name it, print_even_odd()
# inside the method, get an input from the prompt of a number
# val = int(input("Enter number: "))
# print if the value is even or odd.
# i.e. if 2 is entered, print("even"). if 3 is entered , print("odd")
# This has to be in a loop and if -1 is entered, break out the loop.
# To loop infinitely, use the approach of ,  while ( True ): 
