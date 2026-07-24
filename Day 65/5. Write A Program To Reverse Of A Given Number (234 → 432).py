#Write A Program To Reverse Of A Given Number (234 → 432)

n=int(input("Enter a number:"))
revno=0
temp=n
while temp>0:
    d=temp%10
    revno=revno*10+d
    temp=temp//10
print(f"Reverse of {n} is:{revno}")
