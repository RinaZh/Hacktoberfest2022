print("Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.")
print("Find the sum of all the multiples of 3 or 5 below 1000.")
check = 3
summation = 0
while check < 1000:
    if check % 3 == 0 or check % 5 == 0:
       summation += check
    check += 1
print()
print("The sum of all multiples of 3 or 5 below 1000 is " + str(summation))