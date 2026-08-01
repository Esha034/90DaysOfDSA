*
* *
* * *
* * * *
* * * * *

'''
Intuition:

I use two nested loops. The outer loop controls the number of rows and runs from 1 to n.
For each row i, the inner loop runs from 1 to i, so it prints exactly i stars.
After the inner loop finishes, I use print() to move the cursor to the next line. 
Therefore, the number of stars increases by one in every row.
'''
n=int(input("Enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
        
    # Move to the next line after completing one row
    print()

Complexity:

TC-O(n2)
sc-O(1)
