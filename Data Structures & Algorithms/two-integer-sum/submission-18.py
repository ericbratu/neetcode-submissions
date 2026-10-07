class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums):
            hashset[n] = i

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hashset and hashset[diff] != i:
                return [i, hashset[diff]]
