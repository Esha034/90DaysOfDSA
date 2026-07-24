#Write A Program To Find The Sum Of Digit Of A Given Number ( 345 →3+4+5=12)

n=int(input("Enter a number:"))
temp=n
sum=0
while temp>0:
    d=temp%10
    sum+=d
    temp//=10
print(f"Sum of digits of {n} is:{sum}")
