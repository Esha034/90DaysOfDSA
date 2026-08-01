'''
"An Armstrong number is a number that is equal to the sum of its digits, 
where each digit is raised to the power of the total number of digits."


My approach has two main steps :

First, I count the total number of digits.
Second, I extract each digit from the number, raise it to the power of the digit count, and add the results.

Finally, I compare the calculated sum with the original number.
If both are equal, the number is an Armstrong number.”'''

n = int(input("Enter a non-negative number: "))

original = n

# Count the number of digits
if n == 0:
    total_digits = 1
else:
    total_digits = 0
    temp = n

    while temp > 0:
        total_digits += 1
        temp //= 10

# Calculate the Armstrong sum
temp = n
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** total_digits
    temp //= 10

# Handle zero
if n == 0:
    armstrong_sum = 0

# Compare with the original number
if original == armstrong_sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
