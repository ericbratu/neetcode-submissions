class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, n in enumerate(nums):
            if n != i:
                return n - 1

            if n == len(nums) - 1:
                return n + 1