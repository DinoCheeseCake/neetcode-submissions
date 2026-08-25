class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        return max(hm, key = hm.get)