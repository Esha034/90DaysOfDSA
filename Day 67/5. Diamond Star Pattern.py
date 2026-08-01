      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
#Intuition:

I divide the diamond into two parts: an upper full pyramid and a lower inverted pyramid. 
For the upper pyramid, the number of leading spaces is n - i, and the number of stars is 2i - 1.
Therefore, the spaces decrease by one and the stars increase by two in every row.

For the lower half, I start from the row after the middle row to avoid printing the widest row twice. 
The number of leading spaces is i, and the number of stars is 2(n - i) - 1. 
Therefore, the spaces increase by one and the stars decrease by two in every row.

  #code
  
n = int(input("Enter the number of rows: "))

for i in range(1,n+1):
    
    for j in range(n-i):
        print("  ",end="")
        
    for j in range(2*i-1):
        print("*",end=" ")
        
    print()

for i in range(1, n):
    
    for j in range(i):
        print("  ",end="")
        
    for j in range(2*(n-i)-1):
        print("*",end=" ")
    print()

Time Complexity=O(n2)
Space Complexity=O(1)
    
