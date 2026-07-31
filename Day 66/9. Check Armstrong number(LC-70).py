''An Armstrong number is a numberthat is equal to the sum of each of its digits raised to the power of the total number of digits.


My approach has two main steps :

First, I count the total number of digits.
Second, I extract each digit from the number, 
raise it to the power of the digit count, and add the results.

Finally, I compare the calculated sum with the original number.
If both are equal, the number is an Armstrong number.”'''

n = int(input("Enter a number: "))
# Store the original number
temp1 = n
# Count total digits
total_digits = 0

while temp1 > 0:
    total_digits += 1
    temp1 //= 10

# Calculate the Armstrong sum
temp = n
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** total_digits
    temp //= 10

# Check whether the number is an Armstrong number
if n == armstrong_sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
