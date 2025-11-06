class Solution:
    def frequencySort(self, s: str) -> str:
        n=len(s)
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        buckets=[[] for _ in range(n+1)]
        for char,freq in freq.items():
            buckets[freq].append(char)

        res=[]
        for freq in range(n,0,-1):
            if buckets[freq]:
                for char in buckets[freq]:
                    res.append(char*freq)
        return "".join(res)
        




#bruteforce

        count={}
        #hashmap to store the freq of char
        for ch in s:
            count[ch]=count.get(ch,0)+1

        #converting hashmap to list of (Char,freq) pair.
        list_of_pairs=list(count.items())
        # Sort the list by frequency in descending order
        list_of_pairs.sort(key=lambda item:item[1],reverse=True)

        res=[]
        for ch,freq in list_of_pairs:
            res.append(ch*freq)
        return "".join(res)


        
