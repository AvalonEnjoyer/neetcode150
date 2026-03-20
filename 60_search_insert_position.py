from typing import List

# Solution 1 - 100% runtime and 99.67% memory
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

# nums=[-1,0,2,4,6,8]
# target=5

# nums=[10,20,30,40,50]
# target=35