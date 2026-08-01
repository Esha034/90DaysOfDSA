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

    # Target is in the left half
    elif target < nums[middle]:
        right = middle - 1

    # Target is in the right half
    else:
        left = middle + 1


if found_index != -1:
    print("Element found at index:", found_index)
else:
    print("Element not found")
