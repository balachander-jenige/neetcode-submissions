class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        if len(s)==len(t):
            for l in s:
                if l in t:
                    t.remove(l)
            if len(t)!=0:
                return False
            else:
                return True
        else:
            False
        