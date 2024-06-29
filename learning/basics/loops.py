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