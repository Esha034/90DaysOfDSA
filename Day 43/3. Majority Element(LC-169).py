#optimal (Boyer-Moore)

nums = list(map(int, input().split()))

count = 0
candidate = None

for num in nums:
    if count == 0:
        candidate = num
    
    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)

# Complexity:
# Time Complexity: $O(n)$ — We only pass through the array exactly once.
# Space Complexity: $O(1)$ — We only use two variables (candidate and count), requiring constant extra space.
#better
 # from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        from collections import defaultdict
        freq=defaultdict(int)
        
        for num in nums:
            freq[num]+=1
            
        for key in freq:
            if freq[key]>n//2:
                return key
# Complexity:
# Time Complexity: $O(n)$ because we iterate through the list of size $n$ twice.
# Space Complexity: $O(n)$ because in the worst-case scenario, we store up to $n$ unique elements in the dictionary.
#better

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        mp={}
        for i in range(n):
            if nums[i] in mp:
                mp[nums[i]]+=1

            else:
                mp[nums[i]]=1

        for key in mp:
            if mp[key]>n//2:
                return key
