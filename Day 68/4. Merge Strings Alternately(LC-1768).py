#intuition-

I use two pointers, where i points to the current character of word1 and j points to the current character of word2.
While both pointers are within their respective strings, I append one character from word1 followed by one character from word2.
Then, I increment both pointers. After one string is exhausted, I append all the remaining characters from the longer string.
Finally, I join the list of characters and return the merged string.

#code

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)

        merged=[]
        i,j=0,0
        while i<n1 and j<n2:
            merged.append(word1[i])
            merged.append(word2[j])

            i+=1
            j+=1

        while i<n1:
            merged.append(word1[i])
            i+=1
        while j<n2:
            merged.append(word2[j])
            j+=1
        return "".join(merged)

  character is processed exactly once.

Time Complexity=O(n+m)
Space Complexity=O(n+m)
	​


        
