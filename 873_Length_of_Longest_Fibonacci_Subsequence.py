#Question:
#A sequence x1, x2, ..., xn is Fibonacci-like if:
#			n >= 3
#			xi + xi+1 == xi+2 for all i + 2 <= n
#Given a strictly increasing array arr of positive integers forming a sequence, 
#return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
#A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, 
#without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
#Author:	Jiawen Liu

#Solution 1: python3
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        a = set(arr)
        n = len(arr)
        result = 0
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                count = 2
                x, y = arr[i], arr[j]
                while x + y in a:
                    x,y = y, x+y
                    count += 1
                result = max(count,result)
        return result if result > 2 else 0
		
		
#Solution 2:
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        a = set(arr)
        n = len(arr)
        lengths = [[2]*(n) for _ in range(n)]
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                next = arr[j] + arr[i]
                if next in a:
                    k = arr.index(next)
                    lengths[j][k] = lengths[i][j] +1
                    result = max(result,lengths[j][k])
        return result if result > 2 else 0
                    
"""

		
		