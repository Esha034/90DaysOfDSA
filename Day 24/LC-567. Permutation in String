class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1, L2 = len(s1), len(s2)
        if L1 > L2:
            return False
    # 1. Initialize frequency maps for s1 and the first window of s2
        map1 = [0] * 26
        map2 = [0] * 26

    #2. Fill maps for s1 & first window of s2
        for i in range(L1):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1

        if map1 == map2:
            return True

    # 3. Slide the window from index L1 to the end
        for i in range(L1, L2):
        
            map2[ord(s2[i]) - ord('a')] += 1
            map2[ord(s2[i - L1]) - ord('a')] -= 1
        
    # 4.Check for a match after the slide 
            if map1 == map2:
                return True

        return False



#better
        l1,l2=len(s1),len(s2)
        if l1> l2:
            return False
    
        map1=[0]*26
        for char in s1:
            map1[ord(char)-ord('a')]+=1

        for i in range(l2-l1+1):
            map2=[0]*26
            sub=s2[i:i+l1]
            for char in sub:
                map2[ord(char)-ord('a')]+=1
            if map1==map2:
                return True
        return False
        
    
        
