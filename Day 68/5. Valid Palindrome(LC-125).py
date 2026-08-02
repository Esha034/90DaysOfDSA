Intuition-
I use two pointers, one starting from the beginning and the other from the end. 
I skip all non-alphanumeric characters because they should not affect the palindrome check.
I compare the remaining characters without considering case.
If any pair is different, I return False. Otherwise, I move both pointers toward the center. 
If all valid character pairs match, I return True.


#code

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l,r=0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

Time Complexity=O(n)
Auxiliary Space Complexity=O(1)
	​
