# Write A Program To Swap Two Numbers

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

print("Before Swapping:")
print(f" 1st number={a}")
print(f" 2nd number={b}")

temp=a
a=b
b=temp

print("After Swapping:")
print(f" 1st number={a}")
print(f" 2nd number={b}")
