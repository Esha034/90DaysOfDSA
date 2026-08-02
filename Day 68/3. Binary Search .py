

#Intuition-
Binary search works only on a sorted array.
I initialize two pointers: left at index 0 and right at the last index. 
While left is less than or equal to right, I calculate the middle index. 
If the middle element equals the target, I return its index. 
If the target is smaller than the middle element, I discard the right half by updating right to middle - 1. 
Otherwise, I discard the left half by updating left to middle + 1.
In every iteration, the search space is reduced by approximately half.


    
 #Code
nums = list(map(int, input("Enter sorted numbers: ").split()))

target = int(input("Enter the target element: "))

left = 0
right = len(nums) - 1

found_index = -1

while left <= right:

    # Calculate the middle index
    middle = left + (right - left) // 2

    # Target found
    if nums[middle] == target:
        found_index = middle
        break
  
    elif target < nums[middle]:
        right = middle - 1
    else:
        left = middle + 1


if found_index != -1:
    print("Element found at index:", found_index)
else:
    print("Element not found")


Therefore:

Time Complexity=O(logn)
Space Complexity=O(1)
	​


