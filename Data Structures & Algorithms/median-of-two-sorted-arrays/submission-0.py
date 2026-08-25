class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2  # nums1
            j = half - i - 2  # nums2  
                              # minus 2 cause array start from 0

            A = nums1[i] if i >= 0 else float("-infinity")
            AA = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            B = nums2[j] if j >= 0 else float("-infinity")
            BB = nums2[j+1] if (j+1) < len(nums2) else float("infinity")

            if B <= AA and A <= BB:
                if total % 2 == 1:
                    return min(AA, BB)
                else:
                    return (max(A, B) + min(AA, BB)) / 2
            elif A > BB:
                r = i - 1
            else:
                l = i + 1
        
