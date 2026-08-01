#1. Brute-Force Approach — Create a New Array

#Idea
I create an empty array and traverse the original array from the last index to the first index. During each iteration, I add the current element to the new array. 
Since the elements are copied from right to left, the new array contains the elements in reverse order.
#Python Code
nums = list(map(int, input().split()))

n = len(nums)

reversed_nums = []

# Start from the last index
for i in range(n - 1, -1, -1):
    reversed_nums.append(nums[i])

print(reversed_nums)



#Complexity
Time Complexity=O(n)
Space Complexity=O(n)
	​


#2. Better Approach — Using a Stack

#Idea
I use a stack because it follows the Last In, First Out principle.
First, I push every array element onto the stack. 
Then, I repeatedly pop elements and store them in a new array.
Since the last inserted element is removed first, the elements are obtained in reverse order.

#Python Code
nums = list(map(int, input().split()))

stack = []

# Push all elements into the stack
for i in range(len(nums)):
    stack.append(nums[i])

reversed_nums = []

# Pop elements from the stack
while len(stack) > 0:
    reversed_nums.append(stack.pop())

print(reversed_nums)

#3. Optimal Approach — Two Pointers ✅

This is the approach you wrote.

#Idea

I use two pointers, where the left pointer starts at index 0 and the right pointer starts at the last index.
In every iteration, I swap the elements at the two pointers. 
Then, I increment the left pointer and decrement the right pointer.
I continue until the pointers meet or cross. This reverses the array in place without using an additional array.


#code

nums=list(map(int,input().split()))
n=len(nums)
l,r=0,n-1
while l<r:
    nums[l],nums[r]=nums[r],nums[l]
    l+=1
    r-=1
    
print(nums)

Time Complexity=O(n)
Auxiliary Space Complexity=O(1)
	​
