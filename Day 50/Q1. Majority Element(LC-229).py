#optimal 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2=0
        candidate1=candidate2=None
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1

            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
        
            else:
                count1-=1
                count2-=1
        res=[]
        n=len(nums)
        if nums.count(candidate1)>n//3:
            res.append(candidate1)
        if candidate2!=candidate1 and nums.count(candidate2)>n//3:
            res.append(candidate2)
        return res




#bruteforce

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mp={}
        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
        res=[]
        for key in mp:
            if mp[key]>n//3:
                res.append(key)
        return res
