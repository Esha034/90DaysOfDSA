
#optimal code

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



#better approach

'''Intuition- I initialize the first two Fibonacci numbers as 0 and 1. 
Then, for each term, I print the current first number. 
I calculate the next Fibonacci number by adding the previous two numbers and update both variables.
This generates the series iteratively without using extra space.'''

n = int(input("Enter the number of terms: "))

first = 0
second = 1

for i in range(n):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number



#Complexity
Time Complexity: O(n)
The loop runs n times.
Space Complexity: O(1)
Only a few variables are used.
