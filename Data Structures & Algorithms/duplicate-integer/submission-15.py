class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        length = len(nums)
        for i in range(length):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        return False