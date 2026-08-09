#Approach 1 — Brute Force

Idea
Square every element.
Sort the squared array.
Return the result.

#Code
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        # Square every element
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        # Sort the squared array
        nums.sort()

        return nums

Time Complexity=O(nlogn)
Auxiliary Space Complexity=O(1)
	​


Approach 3 — Optimal Two-Pointer Approach 

Idea:
Since the input array is already sorted, the largest absolute value must be present at either the left end or the right end. 
I use two pointers, one at the beginning and one at the end. I compare the squares of both values and place the larger square at the current last position of the result array.
Then I move the corresponding pointer inward and continue filling the result from right to left. 
This avoids sorting and processes every element only once.

Because the array is sorted:

[-7, -3, 2, 3, 11]
 ↑                 ↑
left             right

The largest absolute value must be at one of the ends.

#Optimal Code

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        l,r=0,n-1
        position=n-1

        while l<=r:
            if nums[l]>nums[r]:
                ans[position]=nums[l]
                l+=1
            else:
                ans[position]=nums[r]
                r-=1
            position-=1
        return ans
