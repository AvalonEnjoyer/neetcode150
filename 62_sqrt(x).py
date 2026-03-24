# Solution 3 - 74.26% runtime and 67.62% memory
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while l<=r:
            mid=(r+l)//2
            if x//mid>mid:
                l = mid + 1
            elif x//mid<mid:
                r = mid - 1
            else:
                return mid
        return r

# Solution 2 - 100% runtime and 99.25% memory
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while l<=r:
            mid=(r+l)//2
            sqr = mid*mid
            if sqr>x:
                r = mid - 1
            elif sqr<x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res

# Solution 1 - 74.25% runtime and 99.25% memory
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        l = 1
        r = x
        while l<=r:
            mid=(r+l)//2
            sqr = mid*mid
            if sqr==x:
                return mid
            elif sqr>x:
                r = mid - 1
            else:
                l = mid + 1
        return r