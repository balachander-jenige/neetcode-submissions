class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        newstr=""
        right=0
        while right <len(s):
            if s[right] not in newstr:
                newstr += s[right]
            else:
                newstr=""
                right=right-1
            maxlen=max(maxlen,len(newstr))
            right= right+1
        return maxlen
        