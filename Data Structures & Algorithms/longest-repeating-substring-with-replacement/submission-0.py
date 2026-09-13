class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        low=0
        maxl=0
        maxf=0
        
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            maxf = max(maxf,freq[s[i]])
            if((i-low+1)-maxf > k):
                freq[s[low]]-=1
                low+=1
            
            maxl=max(maxl,i-low+1)

        return maxl