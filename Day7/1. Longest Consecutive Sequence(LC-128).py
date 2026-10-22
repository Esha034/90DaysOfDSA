class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 0:
            return 0
        hash_set={}
        longest=0
        for num in nums:
            hash_set[num]=True
        for num in nums:
            if (num-1) not in hash_set:
                current=num
                count=1
                while (current + 1) in hash_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest







# #better
#         n=len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if nums[i]>nums[j]:
#                     nums[i],nums[j]=nums[j],nums[i]
#         count=1
#         longest=0
#         for i in range(1,n):
#             if nums[i]==nums[i-1]+1:
#                 count+=1
#                 longest=max(count,longest)
#             elif nums[i] != nums[i-1]:  # reset only if not duplicate
#                 count=1
#         return longest




# #Bruteforce
#         n = len(nums)
#         if n == 0:
#             return 0

#         longest = 0
#         for i in range(n):
#             current = nums[i]
#             count = 1
#             # Keep checking next numbers
#             while (current + 1) in nums:  # O(n) search
#                 current += 1
#                 count += 1
#             longest = max(longest, count)
#         return longest

      
        




        
