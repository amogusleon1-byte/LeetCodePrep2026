class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash = {}

        for index, num in enumerate(nums):
            diff = target - num
            if num not in diff_hash:
                diff_hash[diff] = index
            else:
                return [diff_hash[num], index]

        # Should never get to this case
        return [0,0]
