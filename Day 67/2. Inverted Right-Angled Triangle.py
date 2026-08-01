* * * * *
* * * *
* * *
* *
*


n=int(input("Enter no. of rows:"))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
        
    # Move to the next line after completing one row
    print()

#complexity
TC-O(n²)
SC-O(1)
