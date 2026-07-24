
n=int(input("Enter a number:"))
factorial=1

for i in range(1,n+1):
    factorial=factorial*i
    
print(f"factorial of {n} is:{factorial}")


#Using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
        
    return n*factorial(n-1)  
n=int(input("Enter a number:"))
print(f"Factorial of {n} is:", factorial(n))
