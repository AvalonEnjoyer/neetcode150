from typing import List

# Solution 2 - 100% runtime and 100% memory
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]


# Solution 1 - 100% runtime and 100% memory
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            print(f"L: {nums[l]}, R: {nums[r]}, Mid: {nums[mid]}")
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid-1
        print(l, r, mid)
        return nums[l]
