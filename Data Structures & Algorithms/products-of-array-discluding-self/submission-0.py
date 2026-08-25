class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zerocnt = 0
        zero_idx = []
        for i, n in enumerate(nums):
            if n:
                prod *= n
            else:
                zerocnt += 1
        if zerocnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if zerocnt:
                if not n:
                    res[i] = prod
            else:
                res[i] = prod // n

        return res