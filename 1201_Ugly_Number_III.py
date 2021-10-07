#1201. Ugly Number III
#An ugly number is a positive integer that is divisible by a, b, or c.
#Given four integers n, a, b, and c, return the nth ugly number.

 
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if a > b or b > c:
            arr = sorted([a,b,c])
            return self.nthUglyNumber(n, arr[0], arr[1], arr[2])
        
        lcm_abc = math.lcm(a,b,c)
        lcm_ab = math.lcm(a,b)
        lcm_bc = math.lcm(b,c)
        lcm_ac = math.lcm(a,c)
        gcd_abc = math.gcd(a,b,c)

        r = n*a
        temp = n*a - (numUgly(n*a,a,b,c,lcm_abc,lcm_ab,lcm_bc,lcm_ac) - n)*a
        l = numUgly(temp,a,b,c,lcm_abc,lcm_ab,lcm_bc,lcm_ac)
		
        while l < r:
            mid = int(l + (r-l)/2)
            num = numUgly(mid,a,b,c,lcm_abc,lcm_ab,lcm_bc,lcm_ac)
            if num < n:
                l = mid + 1
            else:
                r = mid
        return l
    
def numUgly(result,a,b,c,lcm_abc,lcm_ab,lcm_bc,lcm_ac):
    return int(result/a)+int(result/b) + int(result/c) - int(result/lcm_bc) - int(result/lcm_ab) -  int(result/lcm_ac) +  int(result/lcm_abc)

    