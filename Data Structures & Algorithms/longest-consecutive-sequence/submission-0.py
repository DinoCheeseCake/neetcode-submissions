class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        res = 0
        for num in nums:
            
            # check if num-1 is in sequence <= the start of the seq
            if (num-1) not in nums:
                length = 1
                while (num+length) in nums:
                    length += 1
                res = max(res, length)

        return res

