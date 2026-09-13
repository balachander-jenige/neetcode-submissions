class Solution:
    def maxArea(self, h: List[int]) -> int:
        low=0
        maxarea = 0
        for i in range(len(h)):
            hgt=min(h[low],h[i])
            area=(i-low)*hgt
            if h[low] < h[i]:
                low=i
            maxarea=max(maxarea,area)

        return maxarea
        