class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)

        return False if len(set(nums)) == len(nums) else True