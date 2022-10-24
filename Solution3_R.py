print("For a positive integer k, define d(k) as the sum of the digits of k. Thus d(42) = 4+2 = 6.")
integer = int(input("Please enter a positive integer: "))
first_integer = integer
summation = 0
while integer >= 10:
    summation += integer % 10
    integer = integer // 10
summation += integer
print()
print("The sum of the digits of " + str(first_integer) + " is equal to " + str(summation))