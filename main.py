# imports
import math

# list of numbers to divide by
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# starting number
x = 1

# main loop to increment x and check it
while x > 0:
    print(x)
    no_remainder = True

    # divide each number in 'numbers' list by  the current value of x
    for num in numbers:
        if math.remainder(x, num) != 0.0:

            # change value of 'no_remainder' if the operation has a remainder and move the loop to the next number
            no_remainder = False
            break
    
    # check value of 'no_remainder' variable
    if no_remainder == True:
        print(x)
        break
    x += 1
