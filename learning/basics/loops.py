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

Enter a number to loop through a range: 20
Enter a number that is a divisor: 3
[1..20]
1: is 1 divisible by 3 ? print 1
2: is 2 divisible by 3 ? print 2
3: is 3 divisible by 3 ? print 3
'''

upper_limit = int(input("Enter upper limit: "))
divisor = int(input("Enter divisor: "))

for number in range(1, upper_limit + 1):
    if number % divisor == 0:
        print(number)
        
'''
Now, implement the above using while loop.
'''
print("Implementing the above with a while loop...")
start = 1
while start <= upper_limit:
    if start % divisor == 0:
        print(start)
    start += 1
    
    
'''
In order to quit the loop without completing it, we need to "break" from the loop.
This can be using a break statement.
For e.g. in the below while loop, we just get into the loop and then break from it.
'''

print("We are about to get into a loop and then come out of it without completing the loop for 10 times")
start = 1
while start <= 10:
    print("hello")
    start = start + 1
    break

print("We are out of the loop!!!")


'''
Excercise: 2-Jul-2024
loop through with start = 1 and with a upper limit of 1000.
take an input of a number at which the loop should be break.
meanwhile, within the loop, print the word "hello".
10

20
1001
'''
start = 1
print ("We are now in the loop")
upper_limit = int(input("Enter upper_limit: "))
Loop_until = int(input("Enter Divisor: "))
print (f"You entered the upper_limit: {upper_limit} ")
print (f"You have entered the Divisor: {Loop_until} ")

while start <= upper_limit:
    print("Hello!")
    if start >= Loop_until: break
    start = start + 1
#if divisor > upper_limit == print("You have printed the divisor: "):
  # if upper_limit > Divisor == print ("You have printed upper_limit:"):