class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Get the target hash
        target_hash = {}


        # Iterate over the index and number in the num list
        for index, num in enumerate(nums):

            # Store the current iteration difference of the target minus the number
            diff = target - num
            
            # If difference is not in hash, store the number and index
            if diff not in target_hash:
                target_hash[num] = index
            else:
                # Otherwise we have a matching pair, get the index of the existing diff in hash and the current hash 
                # as the answer
                return [target_hash[diff], index]


        # Time Complexity: O(N) -  at worst need to iterate across all n elements in nums
        # Space Complexity: O(N) - at worst hash map needs to store n-1 elements till we have matching sum
