class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1
        maxarea = 0

        while left < right:

            area = min(heights[left], heights[right])*(right-left)
            if area > maxarea:
                maxarea = area
            left += 1

            if left == right:
                left = 0
                right -= 1
        
            if left == right == 0:
                break
        
        return maxarea