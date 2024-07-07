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
    print(f"Upper limit:{upper_limit}\nWe are looping until:{loop_until_value}")
    start = 1

    while start <= upper_limit:
        print("Hello!")
        if start >= loop_until_value: break
        start = start + 1


loop_until( 5, 3 )
loop_until( 6, 3)
loop_until(5, 10 )
loop_until( -1, 10 )