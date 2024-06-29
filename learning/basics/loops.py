'''
A code is not just about processing the statements one after the other.
Sometimes, we need to loop through the same statements until the condition is met.
Loops are
 - for
 - while
'''

''' 
while loop: for a start, check the condition is met. step.
 Step1: start = 1
 Step2: check if start < 10
 do work
 increment start by 1
 go to step#2
'''

'''
print "hi" 10 times by using a while loop
'''
start = 1
while start <= 10:
    print(f"{start}: Hi")
    start = start + 1

'''
write a while loop that skips 1 counter and loops till it is less than 20 and within the loop, it prints the number.
'''
start = 1
while start < 20:
    print(f"{start}") 
    start = start + 2
    
'''
A for loop will loop through a range of items. for e.g. numbers, collections.
If you want to loop between 1 to 10, in python, we simply say 1..10
'''
print("Printing numbers between 1 to 10")
for number in range(1, 11):
    print(number)
    
''' 
Range also takes another argument that handles the step. By default it is 1. 
To skip 1 number in a for loop range, we use the step = 2
'''
print("Printing from 1 to 10 and skipping 1 number between the numbers")
for number in range(1, 11, 2):
    print(number)
    
'''
Take input of the range of numbers between 1 to <input> and print a number that is perfectly divisible by a <input> number.
'''

'''
get the input of a range.
get the divisor as the input.
loop through till the range
for each of that number in the range, check if the number is perfectly divisible by the divisor.
if yes, print the number.
'''

