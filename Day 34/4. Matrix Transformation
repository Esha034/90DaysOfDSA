Given:

A square matrix of size N × N
Each element is an integer

Goal:To replace every element with:
The nearest number divisible by 5
# code
n=int(input())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        x=matrix[i][j]
        lower=(x//5)*5
        higher=lower+5
        if abs(x-lower)<=abs(x-higher):
            matrix[i][j]=lower
        else:
            matrix[i][j]=higher
            
# 🔽 Output with trailing space
for row in matrix:
    for val in row:
        print(val, end=" ")   # ensures space after each element
    print()   # move to next line
