   * 
  * * * 
 * * * * * 
* * * * * * * 

Intuition:
         
I use three loops. The outer loop controls the number of rows. 
For every row i, the first inner loop prints n - i leading spaces, so the number of spaces decreases by one in each row.
The second inner loop prints 2 × i - 1 stars, which generates the sequence 1, 3, 5, 7, .... 
After completing each row, I use print() to move to the next line. 
This produces a centered full-star pyramid.

#code
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    # Print leading spaces
    for j in range(n - i):
        print("  ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end=" ")

  herefore:

Time Complexity=O(n2)
Space Complexity-O(1)
	​

    # Move to the next row
    print()
