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
