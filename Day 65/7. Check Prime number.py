#Write A Program To check whether A Given Number is prime or not prime number.
#optimal approach
import math
n=int(input("Enter a number:"))
is_prime=True
if n<2:
    print("Not a prime number")
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")






#better approach


n=int(input("Enter a number:"))
is_prime=True
if n<2:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")
        
