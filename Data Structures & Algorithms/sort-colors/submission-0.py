class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        k = 0
        for i in sorted(hm.keys()):
            for _ in range(hm[i]):
                nums[k] = i
                k += 1
        