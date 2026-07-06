from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        res=[]
        for word in strs:
            sorted_s=tuple(sorted(word))
            anagram_map[sorted_s].append(word)
        for v in anagram_map.values():
            res.append(v)
        return res



            
        
        