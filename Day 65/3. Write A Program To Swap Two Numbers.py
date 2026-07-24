#  using third variable

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









# withoust using third variable
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

print("Before Swapping:")
print(f" 1st number={a}")
print(f" 2nd number={b}")

a=a+b
b=a-b
a=a-b

print("After Swapping:")
print(f" 1st number={a}")
print(f" 2nd number={b}")
