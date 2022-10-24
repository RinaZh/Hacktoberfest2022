print("Calculate the sum of the squares of all the divisors of a positive integer.")
print("For example: The divisors of 6 are 1,2,3 and 6. The sum of the squares of these numbers is 1+4+9+36=50.")
integer = int(input("Enter a positive integer: "))
check = 1
summation = 0
while check <= integer/2:
    if integer % check == 0:
        summation += check ** 2
    check += 1
summation += integer ** 2
print()
print("The sum of the square of all the divisors of " + str(integer) + " is " + str(summation))