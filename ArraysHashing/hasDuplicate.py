class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat_hash = {}

        for num in nums:
            if num not in repeat_hash:
                repeat_hash[num] = 1
            else:
                return True

        return False
