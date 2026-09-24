class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in lookup:
                return [lookup[remaining], i]
            lookup[num] = i 


