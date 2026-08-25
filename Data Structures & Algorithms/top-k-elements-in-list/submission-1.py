class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        arr = []
        for num, cnt in hm.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr[-1][1])
            arr.pop()

        return res