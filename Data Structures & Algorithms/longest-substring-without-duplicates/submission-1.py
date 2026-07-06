class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp={}
        l,r=0,0
        maxl=0
        while r <len(s):
            if s[r] in mapp:
                if mapp[s[r]]>=l:
                    l=mapp[s[r]]+1
                    mapp[s[r]]=r
                 

            sl=r-l+1
            if sl>maxl:
                maxl=sl
            mapp[s[r]]=r
            r+=1      

        return maxl