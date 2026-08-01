        *
      *   *
    *       *
  *           *
* * * * * * * * *


Case 1:
First row → Print only one star

Case 2:
Middle rows → Print stars only at the boundaries

Case 3:
Last row → Print stars in every position


#Intuition
I use an outer loop to control the rows. For each row i, I first print n - i leading spaces, so the indentation decreases by one in every row. 
Then, I use another loop that runs 2i - 1 times because each row has an odd number of positions.

I print a star at the first position and the last position to create the left and right boundaries.
For the last row, I print stars at every position to create a filled base. 
For all remaining positions in the middle rows,
I print spaces, which creates the hollow part of the pyramid.


#code


n = int(input("Enter the number of rows: "))

for i in range(1,n+1):
    
     # Print leading spaces
    for j in range(n-i):
        print("  ",end="")
        
    for j in range(1,2*i):
        
         # Print stars in the first and last positions
        # Print stars in every position of the last row
        if j==1 or j==2*i-1 or i==n:
            print("*",end=" ")
        # Print spaces inside the hollow part
        else:
            print(" ",end=" ")
        
    print()

