#bruteforce
n = int(input())
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(total_sum)


#better
n = int(input())

def totalsum(n):
    sum=0
    i=1   
    while i<=n:
        sum+=i
        i+=1
    return sum
print(totalsum(n))



#optimal 
n = int(input())

def totalsum(n):
    return n*(n+1)//2
print(totalsum(n))
    
