#Write A Program To check whether A Given Number is palindrome no. or not 

#optimal approach


num = int(input("Enter a number: "))

if str(num) == str(num)[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")



#better 


def isPalindrome(num):

    original = num
    reverse = 0

    while num > 0:

        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


n = int(input("Enter a number: "))

if isPalindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")







#better approach


n=int(input("Enter a number:"))
temp=n
rev=0
while(temp>0):
    d=temp%10
    rev=rev*10+d
    temp//=10
if rev==n:
    print("Palindrome")
else:
    print("Not Palindrome")














#better approach

n=int(input("Enter a number:"))
temp=n
rev=0
while(temp>0):
    d=temp%10
    rev=rev*10+d
    temp//=10
if rev==n:
    print("Palindrome")
else:
    print("Not Palindrome")



