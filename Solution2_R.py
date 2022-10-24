print("Problem 2: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.")
integer = 1
sumOfSquare = 0
squareOfSum = 0
summation = 0
while integer <= 100:
    sumOfSquare += integer ** 2
    summation += integer
    integer += 1
squareOfSum = summation ** 2
print()
print("The sum of the squares of the first one hundrend natural numbers is " + str(sumOfSquare))
print()
print("The sqaure of the sum of the first one hundred natrul numbers is " + str(squareOfSum))
print()
print("The different between the Square of the Sum and the Sum of the Square is " + str(squareOfSum - sumOfSquare))