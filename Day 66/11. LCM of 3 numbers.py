'''
To find the LCM of three numbers, I first use the relationship between LCM and GCD.

For two numbers, the formula is:
             LCM(a,b)= ∣a×b∣ // gcd(a,b)

To calculate the GCD efficiently, I use the Euclidean algorithm.
The idea is that the GCD of two numbers remains unchanged if the larger number is replaced by its remainder when divided by the smaller number.
In every iteration, I replace a with b and replace b with a % b. I continue until b becomes zero. At that point, a contains the GCD. 

Formula: 
              gcd(a,b)=gcd(b,a mod b)

Since lcm() function works for two numbers, I calculate the LCM of the first two numbers 
and then calculate the LCM of that result with the third number.

Therefore:
    The formula becomes:  LCM(a,b,c)=LCM(LCM(a,b),c)
Finally, I print the resulting LCM.
'''
#optimal approach

# Function to find GCD
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
    
# Function to find LCM of two numbers
def lcm(a,b):
   if a==0 or b==0:
       return 0
   return abs(a*b)//gcd(a,b)
   
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd Number:"))

# Find LCM of the result and third number
ans=lcm(lcm(a,b),c)

print(f"LCM of {a},{b} and {c} is:",ans)




#better 

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd Number:"))
max=a
if b>max:
    max=b
if c>max:
    max=c
   
multiple=max

while True:
    if multiple % a==0 and multiple % b==0 and multiple % c==0:
        break
    multiple+=max

print(f"LCM of {a},{b} and {c} is:",multiple)
