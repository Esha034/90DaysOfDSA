#Intuition

I use an outer loop to control the rows.
For each row i, I use the first inner loop to print i - 1 leading spaces, so the indentation increases by one in every row. 
Then, I use the second inner loop to print 2 × (n - i) + 1 stars.
This generates the sequence 2n - 1, 2n - 3, ..., 1, so the number of stars decreases by two in every row. 
After printing the spaces and stars for one row, I use print() to move to the next line. 
This produces an inverted full-star pyramid.


#Code
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    # Print leading spaces
    for j in range(i-1):
        print(" ", end="")

    # Print stars
    for j in range(2 * (n-i) + 1):
        print("*", end=" ")

    # Move to the next row
    print()
