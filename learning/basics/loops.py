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
print only even numbers less than 10 starting from 1.
'''

start = 0
while start <10:
    print(start)
    start = start + 2

start = 0
times = 1

ulimit = 500000

import time
start_time = time.time()


while start <ulimit:
    print(f" looping in {times}:{start}")
    start = start + 3
    times = times + 1
print("--- %s seconds ---" % (time.time() - start_time))


start = 0
times  = 0
start_time = time.time()
while start <ulimit:
    print(f"Looping in {times}")
    times = times + 1
    if start % 3 == 0:
        print(start)
    start = start + 1

print("--- %s seconds ---" % (time.time() - start_time))
