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

def print_even_odd( ): # type: ignore
   while (True):
        val = int(input("Enter number ( -1 to break out): "))

        if val == -1: break
        if val % 2 == 0:
                print(f"{val}, This number is even") 
                
        else: print(f"{val}, This number is odd")
        
print_even_odd()


# Write a method naming, apply_weights() with 3 arguments. Weight1, Weight2 and amount
# you need to calculate the portion for each weight that is passed.
# For e.g., if we call the method apply_weights( 5, 7, 840 )
# You need to apply 5 : 7 on 840 and then print it as 
# 5 / 12 of 840 = 350
# 7 / 12 of 840 = 490
#Reference:
#print (f"First weight( {weight1}/{total_weight} * {value}) = {first_weight}\nSecond weight( {weight2}/{total_weight} * {value} ) = {second_weight}") 

def print_weights(weight_name, weight, total_weight, value,calculated_weight ):
    print(f"{weight_name}( {weight}/{total_weight} * {value}) = {calculated_weight}")

def apply_weights(weight1, weight2,value ):  
    total_weight = weight1 + weight2
    first_weight  = (weight1 / total_weight) * value
    second_weight = (weight2 / total_weight) * value
    print_weights("First weight", weight1, total_weight, value, first_weight)        
    print_weights("Second weight", weight2, total_weight, value, second_weight)        
    


apply_weights(80,40,300)
apply_weights( 20, 80, 400 )

# fw ( 80 / 120) * 300 = 200


# write a method to accept parameter of number.
# This number is an upper limit.
# For e.g., 5
# In the method, you need to start adding from 1 to that number.
# For e.g., you pass 5, then add 1 + 2 + 3 + 4 + 5 = 15
# Print 15 at the end.

def add_upto( ulimit ):
    print(f"In the method add_upto. {ulimit} got passed to the method")
    start = 0
    
    while ( ulimit > 0 ):
        start = start + ulimit
        ulimit = ulimit -1
    
    print(start)
    

add_upto(5)
add_upto(10)
add_upto(1000)
