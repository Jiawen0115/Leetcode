#4. Median of Two Sorted Arrays
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        k = int((n1 + n2 + 1)/2)
        l, r = 0, n1
        while l < r:
            m1 = int(l + (r - l)/2)
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1
        m1, m2 = l, k - l
        c1 = max(-math.inf if m1 <= 0 else nums1[m1-1],
                 -math.inf if m2 <= 0 else nums2[m2-1])
        c2 = min(math.inf if m1 >= n1 else nums1[m1],
                 math.inf if m2 >= n2 else nums2[m2])
        if (n1+n2)%2 == 1:
            return c1
        else:
            return (c1+c2)/2