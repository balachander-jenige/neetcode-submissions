class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        newstr=""
        right=0
        while right <len(s):
            if s[right] not in newstr:
                newstr += s[right]
            else:
                maxlen=max(maxlen,len(newstr))
                newstr=""
                right=right-1
            right= right+1
        return maxlen
        