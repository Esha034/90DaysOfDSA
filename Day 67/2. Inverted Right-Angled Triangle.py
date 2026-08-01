* * * * *
* * * *
* * *
* *
*

Intuition-
   I use nested loops. The outer loop controls the rows and runs n times. 
For each row i, the inner loop runs n - i times, so the number of stars decreases by one in every row.
The total number of star-printing operations is n + (n - 1) + ... + 1, which is n(n + 1)/2. 
Therefore, the time complexity is O(n²).
Since I use only a constant number of variables, the auxiliary space complexity is O(1).

n=int(input("Enter no. of rows:"))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
        
    # Move to the next line after completing one row
    print()

#complexity
TC-O(n²)
SC-O(1)
