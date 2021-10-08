# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid
# number catch it with a try/except and put out an appropriate message
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Desired output:
# Invalid input
# Maximum is 10
# Minimum is 2

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break #if im all done I break
    try:
        nu = int(num)
    except:
        print('Invalid input')
        continue #if there is a problem I print a message out and I got back up to the top

    if largest is None :
        largest = nu
    elif nu > largest :
        largest = nu
        # print(largest)

    if smallest is None :
        smallest = nu
    elif nu < smallest :
        smallest = nu
        # print(smallest)



print("Maximum is", largest)
print("Minimum is", smallest)


# My output:
# Invalid input
# Maximum is 10
# Minimum is 2
