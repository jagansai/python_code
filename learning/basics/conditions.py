'''
 A program runs with a certain flow.
 Not always we needed to process every line of code.
 Sometimes, as per conditions we would have to skip the line of code.
 For e.g., if we were to print "yes" if a value is greater 10 and "no" 
 if the value were to be less than 10.
 Then, we will have to skip some portion of the code depending on the value.
 
 The conditions in python are , 
    - if
    - elif
    - else
    
    elif has to follow if.
    else should always follow either if or elif
'''

val = 10
# if val > 10 print yes
if val > 10:
    print("yes")
elif val == 10:
    print("maybe")
else:
    print("no")


val = input("Get me a value: ")
print(f"val={val}")

# we will get a value and do some arithmetic ops.

val = int(input("Enter a num: "))

print(f"Add {val} by 10: {val + 10}")

val = int(input("Enter a num: "))
print(f"Subtract {val} by 10: {val - 10}")

val = int(input("Enter a num: "))
print(f"Multiply {val} by 10: {val * 10}")

val = int(input("Enter a num: "))
print(f"Divide {val} by 10: {val / 10}")

val = int(input("Enter a num: "))
print(f"The remainder of {val} when divide by 2: {val % 2}")


val = int(input("Enter a num  to test even or odd: "))
if val % 2 == 0: 
    print("This is a even number")

else:
    print("This is an odd number")  